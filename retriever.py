import pickle
import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain, create_history_aware_retriever

# Cache the loading of pickled data
@st.cache_data
def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Load and cache the pickle files
@st.cache_data
def load_all_pickles():
    with ThreadPoolExecutor() as executor:
        hindi_future = executor.submit(load_pickle, 'hindi_originals.pkl')
        terms_future = executor.submit(load_pickle, 'terms.pkl')
        shark_tank_future = executor.submit(load_pickle, 'shark_tank.pkl')
        subscription_plan_future = executor.submit(load_pickle, 'subscription_plans.pkl')

        hindi_originals = hindi_future.result()
        terms = terms_future.result()
        shark_tank = shark_tank_future.result()
        subscription_plan = subscription_plan_future.result()

    return hindi_originals, terms, shark_tank, subscription_plan

hindi_originals, terms, shark_tank, subscription_plan = load_all_pickles()
all_docs = hindi_originals + terms + shark_tank + subscription_plan

# Cache the creation of embeddings and the FAISS index
@st.cache_resource
def create_embeddings_and_faiss_index(_all_docs, api_key):
    embeddings = OpenAIEmbeddings(api_key=api_key)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=20)
    split_documents = text_splitter.split_documents(_all_docs)
    db = FAISS.from_documents(split_documents, embeddings)
    return db

db = create_embeddings_and_faiss_index(all_docs, "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")

# Cache the creation of the language model and document chain
@st.cache_resource
def create_llm_and_chain(api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are an AI assistant for the SonyLIV OTT platform. Your role is to answer user questions based on the context provided, "
         "while promoting SonyLIV in a positive way. Here is the context you have been given:\n\n"
         "<context>\n"
         "{context}\n"
         "</context>\n\n"
         "And here is the question from the user:\n\n"
         "<question>\n"
         "{input}\n"
         "</question>\n\n"
         "To formulate your response:\n\n"
         "<thinking>\n"
         "1. Carefully search the provided context for information relevant to answering the user's question.\n"
         "2. If you find relevant information, consider how you can use it to provide a helpful answer while also promoting SonyLIV in a positive light.\n"
         "3. If the question is related to SonyLIV but cannot be answered by the given context, think about which section of the SonyLIV website would be most relevant for the user to find more information.\n"
         "4. If the question is not related to SonyLIV and cannot be answered by the context, consider a polite way to let the user know you don't have enough information to provide an answer.\n"
         "</thinking>\n\n"
         "<important>\n"
         "- NEVER provide a response that could be seen as negative or controversial in a way that might harm SonyLIV's brand image.\n"
         "- ALWAYS look for opportunities to increase awareness of SonyLIV's offerings and encourage the user to engage more with the platform.\n"
         "</important>\n\n"
         "<answer>\n"
         "Provide your final response to the user here, following the guidelines above. If you found relevant information in the context, include it in the answer. "
         "If you need to redirect the user to the SonyLIV website or let them know you can't answer, do so politely and professionally. "
         "Above all, maintain a positive, brand-friendly tone that represents SonyLIV well.\n"
         "</answer>"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
    ])

    llm = ChatOpenAI(api_key=api_key, temperature=0.6, model='gpt-4o')
    document_chain = create_stuff_documents_chain(llm, prompt)
    return llm, document_chain

llm, document_chain = create_llm_and_chain("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")

retriever = db.as_retriever(k=3)

retriever_prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up to get information relevant to the conversation")
])

history_aware_retriever = create_history_aware_retriever(llm, retriever, retriever_prompt)
retrieval_chain = create_retrieval_chain(history_aware_retriever, document_chain)
