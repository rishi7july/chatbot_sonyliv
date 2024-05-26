OPENAI_API_KEY = "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"

from langchain_community.document_loaders import WebBaseLoader

# List of URLs to scrape
urls = [
# 'https://www.sonyliv.com/terms-of-use',
# 'https://www.sonyliv.com/privacy-policy',
# 'https://www.sonyliv.com/faqs',
# 'https://www.sonyliv.com/customer-support',
# 'https://advertisewithus.sonyliv.com/?loginType=0&userName=2004242157122496369&firstName=Rishi&lastName=Sharma&profileId=122500953&isChildProfile=false&av=3.5.59&appCode=SONYLIV-WEB-TATA&partnerId=7001',
# 'https://www.sonyliv.com/content-feedback',
# 'https://en.wikipedia.org/wiki/SonyLIV#Current_content_partners'
'https://www.sonyliv.com/subscription?utm_source=google&utm_medium=paid&utm_campaign=in_msixsonyliv_na_performance_alwayson_brand_launch_search_subscriptions_india_apr_2022_v0&utm_content=brandmisspell_kws&utm_term=offerads&gad_source=1&gclid=Cj0KCQjw6auyBhDzARIsALIo6v9cAVDyUPgmKcdbI8vn2NQQUgBjEvCEO3kULvhYmHoDiQO3BPrJJuMaAvTREALw_wcB'
]

# Initialize a list to hold all documents
terms_doc = []

# Iterate over each URL and load the documents
for url in urls:
    loader = WebBaseLoader(url)
    docs = loader.load()
    terms_doc.extend(docs)

# Now `all_docs` contains documents from all the URLs
print(f"Loaded {len(terms_doc)} documents from {len(urls)} URLs.")

import pickle

# Save the all_docs list to a file
with open('terms.pkl', 'wb') as f:
    pickle.dump(terms_doc, f)

print("Documents have been saved to terms.pkl")

print(terms_doc)