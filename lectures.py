# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 18:57:07 2025

@author: Philip Auerbach
"""

# Importing Libaries 
from pandasgui import show 
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from custom_utility.utils import *

#Project file paths
the_path = "/Users/philipauerbach/Desktop/git projects/NLP-SS Class/NLP-SS/git/lectures.py"
the_d_path = "/Users/philipauerbach/Desktop/git projects/NLP-SS Class/NLP-SS/git/data/course_data"

#File paths 
the_data = file_crawler(the_d_path)


the_data["num_tok"] = the_data["body"].apply(
     lambda x: tok_cnt(x, "all"))
the_data["num_tok_u"] = the_data["body"].apply(
     lambda x: tok_cnt(x, "u"))
the_data["body_sw"] = the_data["body"].apply(rem_sw)




# cora_a = " i was fishing the river and caught a bunch of fishes"


# """
# Create a function called stem fun that inputs a corpus and 
# the output is the stemmed version of the original
# """

# def stem_fun(str_input):
#     from nltk.stem import PorterStemmer 
#     ps = PorterStemmer()
#     tmp = str_input.split()
#     stemmed_words = [ps.stem(word) for word in tmp]
#     return ' '.join(stemmed_words)


# print(stem_fun(cora_a))

"""
Create a new column on the_data called body_sw_stem 
where you will aplly stemming on the body_sw column 
use word_fun to get frequency for that new column 
and call the object wrd_fund_body
"""

wrd_fun_body = word_fun(the_data, "body")
wrd_fun_body_sw = word_fun(the_data, "body_sw")

the_data["body_sw_stem"] = the_data["body_sw"].apply(stem_fun)

wrd_fun_body_sw_stem = word_fun(the_data, "body_sw_stem")

ex = "i was fishing last week and caught a hugh brown trout"

# def Lemma_fun(str_corpus):
#     from nltk.stem import WordNetLemmatizer
#     wnl = WordNetLemmatizer()
#     tmp = corpus.split()
#     lemmatized_corpus = [wnl.lemmatize(word)for word in tmp]
#     return ' '.join(lemmatized_corpus)

# def stem_fun(str_input):
#     from nltk.stem import PorterStemmer 
#     ps = PorterStemmer()
#     tmp = str_input.split()
#     stemmed_words = [ps.stem(word) for word in tmp]
#     return ' '.join(stemmed_words)
'''
create one function called stem_fun that can either perform 
PorterStemmer or WordNetLematizer
'''
# def stem_fun(str_corpus, flag):
#     from nltk.stem import WordNetLemmatizer, PorterStemmer

#     if flag == "ps":
#         ps = PorterStemmer()
#         tmp = str_corpus.split()
#         stemmed_words = [ps.stem(word) for word in tmp]
#         return ' '.join(stemmed_words)
    
#     elif flag == "wnl":
#         wnl = WordNetLemmatizer()
#         tmp = str_corpus.split()
#         lemmatized_corpus = [wnl.lemmatize(word)for word in tmp]
#         return ' '.join(lemmatized_corpus)
    
#     else: 
#         print("Error: Please provide a valid flag — 'ps' for PorterStemmer or 'wnl' for WordNetLemmatizer.")
#         return None
    
    

