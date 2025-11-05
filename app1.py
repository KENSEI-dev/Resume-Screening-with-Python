import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

clf=pickle.load(open('clf.pkl','rb'))
tfidfd=pickle.load(open('tfidf.pkl','rb'))

#st.title("Resume Screening App")