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

#Read Data
df = pd.read_csv('twitter.ds.csv',error_bad_lines=False)
comments = df['SentimentText']
opinionLabels = df['Sentiment']
print(len(comments))
print(len(opinionLabels))

