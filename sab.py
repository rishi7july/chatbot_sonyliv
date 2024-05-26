OPENAI_API_KEY = "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"

from langchain_community.document_loaders import WebBaseLoader

# List of URLs to scrape
urls = ['https://en.wikipedia.org/wiki/List_of_programmes_broadcast_by_Sony_SAB',
'https://en.wikipedia.org/wiki/Taarak_Mehta_Ka_Ooltah_Chashmah',
'https://en.wikipedia.org/wiki/Wagle_Ki_Duniya_%E2%80%93_Nayi_Peedhi_Naye_Kissey',
'https://en.wikipedia.org/wiki/Pushpa_Impossible',
'https://en.wikipedia.org/wiki/Dhruv_Tara_%E2%80%93_Samay_Sadi_Se_Pare',
'https://en.wikipedia.org/wiki/Vanshaj',
'https://en.wikipedia.org/wiki/Aangan_%E2%80%93_Aapno_Kaa',
'https://en.wikipedia.org/wiki/Aadat_Se_Majboor_(TV_Series)',
'https://en.wikipedia.org/wiki/Badi_Doooor_Se_Aaye_Hai',
'https://en.wikipedia.org/wiki/Bhakharwadi_(TV_series)',
'https://en.wikipedia.org/wiki/Bhai_Bhaiya_Aur_Brother',
'https://en.wikipedia.org/wiki/Carry_on_Alia',
'https://en.wikipedia.org/wiki/Chidiya_Ghar',
'https://en.wikipedia.org/wiki/Chintu_Chinki_Aur_Ek_Badi_Si_Love_Story',
'https://en.wikipedia.org/wiki/Dr._Madhumati_On_Duty',
'https://en.wikipedia.org/wiki/F.I.R._(TV_series)',
'https://en.wikipedia.org/wiki/Funhit_Mein_Jaari',
'https://en.wikipedia.org/wiki/The_Great_Indian_Family_Drama',
'https://en.wikipedia.org/wiki/Gutur_Gu',
'https://en.wikipedia.org/wiki/Hum_Aapke_Hain_In_Laws',
'https://en.wikipedia.org/wiki/I_Luv_My_India',
'https://en.wikipedia.org/wiki/Jeannie_Aur_Juju',
'https://en.wikipedia.org/wiki/Jijaji_Chhat_Per_Hain',
'https://en.wikipedia.org/wiki/Jijaji_Chhat_Parr_Koii_Hai',
'https://en.wikipedia.org/wiki/Jugni_Chali_Jalandhar',
'https://en.wikipedia.org/wiki/Kaatelal_%26_Sons',
'https://en.wikipedia.org/wiki/Khatmal_E_Ishq',
'https://en.wikipedia.org/wiki/Khidki',
'https://en.wikipedia.org/wiki/Lapataganj',
'https://en.wikipedia.org/wiki/Maddam_Sir',
'https://en.wikipedia.org/wiki/Malegaon_Ka_Chintu',
'https://en.wikipedia.org/wiki/Mangalam_Dangalam',
'https://en.wikipedia.org/wiki/Mrs._%26_Mr._Sharma_Allahabadwale',
'https://en.wikipedia.org/wiki/My_Name_Ijj_Lakhan',
'https://en.wikipedia.org/wiki/Office_Office',
'https://en.wikipedia.org/wiki/Papad_Pol_-_Shahabuddin_Rathod_Ki_Rangeen_Duniya',
'https://en.wikipedia.org/wiki/Partners_Trouble_Ho_Gayi_Double',
'https://en.wikipedia.org/wiki/Peterson_Hill',
'https://en.wikipedia.org/wiki/R._K._Laxman_Ki_Duniya',
'https://en.wikipedia.org/wiki/Sajan_Re_Jhoot_Mat_Bolo',
'https://en.wikipedia.org/wiki/Sajan_Re_Phir_Jhoot_Mat_Bolo',
'https://en.wikipedia.org/wiki/Shrimaan_Shrimati_Phir_Se',
'https://en.wikipedia.org/wiki/Tenali_Rama_(TV_series)',
'https://en.wikipedia.org/wiki/Tera_Yaar_Hoon_Main',
'https://en.wikipedia.org/wiki/Tota_Weds_Maina',
'https://en.wikipedia.org/wiki/Trideviyaan',
'https://en.wikipedia.org/wiki/TV,_Biwi_aur_Main',
'https://en.wikipedia.org/wiki/Yam_Hain_Hum',
'https://en.wikipedia.org/wiki/Yes_Boss_(TV_series)',
'https://en.wikipedia.org/wiki/Zabaan_Sambhalke',
'https://en.wikipedia.org/wiki/Aladdin_%E2%80%93_Naam_Toh_Suna_Hoga',
'https://en.wikipedia.org/wiki/Alif_Laila',
'https://en.wikipedia.org/wiki/Ali_Baba_(TV_series)',
'https://en.wikipedia.org/wiki/Baalveer',
'https://en.wikipedia.org/wiki/Baalveer_Returns',
'https://en.wikipedia.org/wiki/Baalveer_3',
'https://en.wikipedia.org/wiki/Singhasan_Battisi_(TV_series)',
'https://en.wikipedia.org/wiki/Bhanwar_(1998_TV_series)',
'https://en.wikipedia.org/wiki/Dharm_Yoddha_Garud',
'https://en.wikipedia.org/wiki/Dil_Diyaan_Gallaan',
'https://en.wikipedia.org/wiki/Four_(TV_series)',
'https://en.wikipedia.org/wiki/Hero_%E2%80%93_Gayab_Mode_On',
'https://en.wikipedia.org/wiki/Ichhapyaari_Naagin',
'https://en.wikipedia.org/wiki/Jai_Shri_Swaminarayan',
'https://en.wikipedia.org/wiki/Left_Right_Left_(TV_series)',
'https://en.wikipedia.org/wiki/Pashminna_%E2%80%93_Dhaage_Mohabbat_Ke',
'https://en.wikipedia.org/wiki/Sab_Satrangi',
'https://en.wikipedia.org/wiki/Shubh_Laabh_-_Aapkey_Ghar_Mein',
'https://en.wikipedia.org/wiki/Y.A.R.O_Ka_Tashan',
'https://en.wikipedia.org/wiki/Ziddi_Dil_Maane_Na',
'https://en.wikipedia.org/wiki/Movers_%26_Shakers_(TV_series)',
'https://en.wikipedia.org/wiki/Wah!_Wah!_Kya_Baat_Hai!',
'https://en.wikipedia.org/wiki/Alias_(TV_series)',
'https://en.wikipedia.org/wiki/America%27s_Funniest_Home_Videos',
'https://en.wikipedia.org/wiki/Desperate_Housewives',
'https://en.wikipedia.org/wiki/Extreme_Makeover',
'https://en.wikipedia.org/wiki/Home_Improvement_(TV_series)' 
]

# Initialize a list to hold all documents
sab_doc = []

# Iterate over each URL and load the documents
for url in urls:
    loader = WebBaseLoader(url)
    docs = loader.load()
    sab_doc.extend(docs)

# Now `all_docs` contains documents from all the URLs
print(f"Loaded {len(sab_doc)} documents from {len(urls)} URLs.")

import pickle

# Save the all_docs list to a file
with open('sab.pkl', 'wb') as f:
    pickle.dump(sab_doc, f)

print("Documents have been saved to sab.pkl")
