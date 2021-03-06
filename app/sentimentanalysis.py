import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import pickle 
from textblob import TextBlob

def text_process(text):
    '''
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Return the cleaned text as a list of words
    '''
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


def model_predict(inputdata):

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(inputdata)
    yelp = pd.read_csv('yreviews.csv', encoding='utf-8')

    yelp['text length'] = yelp['text'].apply(len)

    yelp_class = yelp[(yelp['opinion'] == 'negative') | (yelp['opinion'] == 'positive')]

    X = yelp_class['text']
    y = yelp_class['opinion']

    bow_transformer = CountVectorizer(analyzer=text_process).fit(X)

    X = bow_transformer.transform(X)

    #from sklearn.model_selection import train_test_split
   # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    #from sklearn.naive_bayes import MultinomialNB
    #nb = MultinomialNB()
    #nb.fit(X_train, y_train)

    #preds = nb.predict(X_test)
    #from sklearn.metrics import confusion_matrix, classification_report
    #print(confusion_matrix(y_test, preds))
    #print('\n')
   # print(classification_report(y_test, preds))
    #review = yelp_class['text'][15]
    #print (review)
    ytb_model = open("senti.pkl","rb")
    new_model = pickle.load(ytb_model)
    t_data = bow_transformer.transform([inputdata])
    sentiment=new_model.predict(t_data) 
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(sentiment)
    return sentiment


def load_modl(inputdata):

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(inputdata)
    yelp = pd.read_csv('yreviews.csv', encoding='utf-8')

    yelp['text length'] = yelp['text'].apply(len)

    yelp_class = yelp[(yelp['opinion'] == 'negative') | (yelp['opinion'] == 'positive')]

    X = yelp_class['text']
    y = yelp_class['opinion']

    bow_transformer = CountVectorizer(analyzer=text_process).fit(X)

    X = bow_transformer.transform(X)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    from sklearn.naive_bayes import MultinomialNB
    nb = MultinomialNB()
    nb.fit(X_train, y_train)

    preds = nb.predict(X_test)
    from sklearn.metrics import confusion_matrix, classification_report
    print(confusion_matrix(y_test, preds))
    print('\n')
    print(classification_report(y_test, preds))
    review = yelp_class['text'][15]
    print (review)
    ytb_model = open("senti.pkl","rb")
    new_model = pickle.load(ytb_model)
    t_data = bow_transformer.transform([inputdata])
    sentiment=new_model.predict(t_data) 
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(sentiment)
    return sentiment


def load_model(inputdata):

    para = (TextBlob(str(inputdata))).polarity
    if float(para) > 0:
	    return 'positive'
    else:
    	return 'negitive'