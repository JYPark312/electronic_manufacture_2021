# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:13:37 2022

@author: young
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize


path_dir = './electronic_manufacture_2021-main/patent_data/cpc_devide/'
file_list = os.listdir(path_dir)

for i in file_list:    
    data = pd.read_csv("./electronic_manufacture_2021-main/patent_data/cpc_devide/"+i)
    
    cpc_list = data['cpc_set']
    
    vect = CountVectorizer()
    document_term_matrix = vect.fit_transform(cpc_list) 
    
    tf = pd.DataFrame(document_term_matrix.toarray(), columns=vect.get_feature_names())
    
    D = len(tf)
    df = tf.astype(bool).sum(axis=0)
    idf = np.log((D+1) / (df+1)) + 1 
    
    tfidf = tf * idf                      
    tfidf_array = tfidf.to_numpy()
    
    co_mat = np.dot(tfidf_array.T, tfidf_array)
    
    feature_name=[]
    for a in vect.get_feature_names():
        feature_name.append(a.upper())
    
    
    co_mat_df = pd.DataFrame(co_mat, columns =feature_name, index = feature_name)
    
    co_mat_df.to_csv("./electronic_manufacture_2021-main/patent_data/network/net_"+i)
