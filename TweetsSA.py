#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:09:24 2017

@author: DangNguyen & DuyTran
"""

import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

df = pd.read_csv("training.1600000.processed.noemoticon.csv")
comments = df['tweet']

#Remove Stop words
stop = stopwords.words('english')

#Test
comments = comments[0:10]

list_vec_words = []
#Split words
for sentence in comments:
    temp_vec_word = []
    for word in sentence.lower().split():
        if word not in stop:
            temp_vec_word.append(word)
    list_vec_words.append(temp_vec_word)

print(comments[0])
print("Split")
print(list_vec_words[0])

#Stemming
st = LancasterStemmer()
for vec_word in list_vec_words:
    for i in range(0, len(vec_word)-1):
        vec_word[i] = st.stem(vec_word[i])
    #Remove Duplicate word
    vec_word = list(set(vec_word))

print("Stemming")
print(list_vec_words[0])

#Remove Username: remove all words start with @
temp_list_words = []
for vec_word in list_vec_words:
    temp_vec_word = []
    for word in vec_word:
        if word[0] != "@":
            temp_vec_word.append(word)
    temp_list_words.append(temp_vec_word)

list_vec_words = temp_list_words
print("Remove Username")
print(list_vec_words[0])

#Remove URL:
temp_list_words = []
for vec_word in list_vec_words:
    temp_vec_word = []
    for word in vec_word:
        word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
        if word != "":
            temp_vec_word.append(word)
    temp_list_words.append(temp_vec_word)

list_vec_words = temp_list_words
print("Remove URL")
print(list_vec_words[0])

#Remove emoticon
list_emoticon = [":)", ":-)", ": )", ":D", "=)", ":(", ":-(", ": ("]

