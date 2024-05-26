OPENAI_API_KEY = "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"

from langchain_community.document_loaders import WebBaseLoader

# List of URLs to scrape
urls = [
    'https://www.sonyliv.com/shows/maharani-1700000725',
    'https://www.sonyliv.com/shows/scam-1992-the-harshad-mehta-story-1700000292',
    'https://www.sonyliv.com/shows/rocket-boys-1700000852', 
    'https://www.sonyliv.com/shows/gullak-1700000659', 
    'https://www.sonyliv.com/shows/tabbar-1700000804', 
    'https://www.sonyliv.com/shows/chamak-hindi-1700001300',
    'https://www.sonyliv.com/shows/college-romance-hindi-1700000667',
    'https://www.sonyliv.com/shows/cubicles-hindi-1700000817',
    'https://www.sonyliv.com/shows/nirmal-pathak-ki-ghar-wapsi-1700000912',
    'https://www.sonyliv.com/shows/shantit-kranti-hindi-1700001317',
    'https://www.sonyliv.com/shows/undekhi-1700000215',
    'https://www.sonyliv.com/shows/scam-2003-the-telgi-story-hindi-1700001283',
    'https://www.sonyliv.com/shows/girls-hostel-1700000681',
    'https://www.sonyliv.com/shows/avrodh-1700000236',
    'https://www.sonyliv.com/shows/the-jengaburu-curse-hindi-1700001260',
    'https://www.sonyliv.com/shows/tanaav-1700000994',
    'https://www.sonyliv.com/shows/cherans-journey-hindi-1700001366',
    'https://www.sonyliv.com/shows/sandwiched-forever-1700000648',
    'https://www.sonyliv.com/shows/pet-puraan-hindi-1700000903',
    'https://www.sonyliv.com/shows/dr-arora-1700000885',
    'https://www.sonyliv.com/shows/potluck-1700000785'
    
]

# Initialize a list to hold all documents
hindi_originals_doc = []

# Iterate over each URL and load the documents
for url in urls:
    loader = WebBaseLoader(url)
    docs = loader.load()
    hindi_originals_doc.extend(docs)

# Now `all_docs` contains documents from all the URLs
print(f"Loaded {len(hindi_originals_doc)} documents from {len(urls)} URLs.")

import pickle

# Save the all_docs list to a file
with open('hindi_originals.pkl', 'wb') as f:
    pickle.dump(hindi_originals_doc, f)

print("Documents have been saved to hindi_originals.pkl")
