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


# the_data["num_tok"] = the_data["body"].apply(
#     lambda x: tok_cnt(x, "all"))
# the_data["num_tok_u"] = the_data["body"].apply(
#     lambda x: tok_cnt(x, "u"))

# the_data["body_sw"] = the_data["body"].apply(rem_sw)

# wrd_fun_body = word_fun(the_data, "body")
# wrd_fun_body_sw = word_fun(the_data, "body_sw")


cora_a = " i was fishing the river and caught a bunch of fishes"


"""
Create a function called stem fun that inputs a corpus and 
the output is the stemmed version of the original
"""

def stem_fun(str_input):
    from nltk.stem import PorterStemmer 
    ps = PorterStemmer()
    tmp = str_input.split()
    stemmed_words = [ps.stem(word) for word in tmp]
    return ' '.join(stemmed_words)


print(stem_fun(cora_a))


