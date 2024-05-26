import pickle
import faiss
import numpy as np
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader

OPENAI_API_KEY = "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"
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)


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
