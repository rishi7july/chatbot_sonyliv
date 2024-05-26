OPENAI_API_KEY = "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"

# In[62]:

from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader('Shark Tank India 2.csv')
shark_tank_doc = loader.load()


import pickle

# Save the all_docs list to a file
with open('shark_tank.pkl', 'wb') as f:
    pickle.dump(shark_tank_doc, f)

print("Documents have been saved to shark_tank.pkl")
