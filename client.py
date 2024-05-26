from retriever import retrieval_chain
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


def process_chat(chain,question,chat_history):
    response = chain.invoke({
        "input":question,
        "chat_history":chat_history
    })
    return response['answer']

#chat_history= []

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         break
#     response  = process_chat(retrieval_chain,user_input,chat_history)
#     chat_history.append(HumanMessage(content=user_input))
#     chat_history.append(AIMessage(content=response))
#     print("Assistant:", response)

## StreamLit app 
import streamlit as st 

# Initialize chat_history if not already in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


st.title("SonyLIV Chat Assistant")

# Display the chat messages in the session state
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.write(message['content'])

# Get user input using streamlit's chat_input
user_input = st.chat_input("Please ask your question: ")


if user_input :
    with st.chat_message('user'):
        st.write(user_input)
    # Add the user message to the chat history
    st.session_state.chat_history.append({'role': 'user', 'content': user_input})

    # Convert chat history to a format suitable for process_chat
    chat_history = [
        HumanMessage(content=msg['content']) if msg['role'] == 'user' else AIMessage(content=msg['content'])
        for msg in st.session_state.chat_history
    ]

    
    # Process the chat and get the response
    response = process_chat(retrieval_chain, user_input, chat_history)
    
    # Add the assistant message to the chat history
    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
    
    # Display the assistant's response
    with st.chat_message('assistant'):
        st.markdown(response)

if __name__ == "__main__":
    main()
