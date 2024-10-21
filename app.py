import streamlit as st
import re
import  nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle

nltk.download('stopwords')


model_filename = "final_model.pkl" 
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

    from sklearn.feature_extraction.text import CountVectorizer
    cvfile = 'BoW.pkl'
    with open(cvfile, 'rb') as file:
      cv = pickle.load(file)


#Website 

st.title('Sentiment Analysis of Restaurant Reviews ')
input_text = st.text_input('Enter the review:')

ps = PorterStemmer()
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
def stemming(text):
    stemmed_text = re.sub('[^a-zA-Z]'," ", text)
    stemmed_text = stemmed_text.lower()
    stemmed_text = stemmed_text.split()
    stemmed_text = [ps.stem(word) for word in stemmed_text if not word in set(all_stopwords)]
    stemmed_text = ' '.join(stemmed_text)
    print("data preproccessed")
    print(stemmed_text)
    return stemmed_text

def prediction(input_text):
    input_text = stemming(input_text)
    input_data = cv.transform([input_text]).toarray()
    prediction = model.predict(input_data)
    return prediction[0]

if input_text:
    pred = prediction(input_text)
    if pred == 1:
        st.write('Positive')
    else:
        st.write('Negative')