OPENAI_API_KEY = "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"

# In[62]:

from langchain_community.document_loaders import TextLoader

loader = TextLoader("subscription_plans.txt")
subscription_plan = loader.load()

import pickle

# Save the all_docs list to a file
with open('subscription_plans.pkl', 'wb') as f:
    pickle.dump(subscription_plan, f)

print("Documents have been saved to subscription_plan.pkl")
