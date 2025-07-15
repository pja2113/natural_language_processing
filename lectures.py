# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 18:57:07 2025

@author: Philip Auerbach
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from custom_utility.utils import *


the_path = "/Users/philipauerbach/Desktop/git projects/NLP-SS Class/NLP-SS/git/lectures.py"
the_d_path = "/Users/philipauerbach/Desktop/git projects/NLP-SS Class/NLP-SS/git/data/course_data"

the_data = file_crawler(the_d_path)

"""
create a function called tok_cnt that accepts a corpus
outputs the number of tokens
"""

# the_data["num_tok"] = the_data["body"].apply(
#     lambda x: tok_cnt(x, "all"))
# the_data["num_tok_u"] = the_data["body"].apply(
#     lambda x: tok_cnt(x, "u"))

# the_data["body_sw"] = the_data["body"].apply(rem_sw)

"""
Create dictionary where the key is the topic
the value is a dictionary that has 2 keys:
    all which is the total number of tokens
    unique which is the unique number of tokens
    
test_dict = {"fishing": {"all": 344, "unqiue": 290},
             "mathematics": {"all": 434, "unqiue": 321}}
"""

#tmp = the_data[the_data["label"] == "fishing"]
# tmp_concat = tmp["body"].str.cat(sep=" ")

# combined = wrd_fun(the_data)

"""
create a dictionary where the key is a unique topic
and the value is the word frequency dictionary key:count
"""

# a = ["the", "cat", "ran", "up", "the", "hill"]

# a_filt = list()
# for word in a:
#     if word != "the":
#         a_filt.append(word)     
# corp = " ".join(a_filt) #package up a list into a single string/corpus

# a_filt_b = [word for word in a if word != "the"] #list comprehension
# corp_a = " ".join(a_filt_b) 

# #dictionary comprehension
# a_dict = dict()
# for word in set(a):
#     a_dict[word] = len(word)

# a = ["the", "cat", "ran", "up", "the", "hill"]
# a_dict = {word:len(word) for word in set(a)}




"""
create a function called rem_sw that removes
all stopwords and returns everything else
ex input: cat in the hat
ex output: cat hat
"""

#t_c = "cat in the hat"
#print (rem_sw("cat in the hat"))

#inline

#test = word_fun(the_data)
#print (tok_cnt("cat cat hat", "u"))

#def tok_cnt_u(c_in):
#    tmp = c_in.split()
#    tmp = len(set(tmp))
#    return tmp

#the_data["num_tok"] = the_data["body"].apply(tok_cnt)
#the_data["num_tok_u"] = the_data["body"].apply(tok_cnt_u)

#sum_stats = the_data.describe()

"""
create a function called tok_cnt_u that accepts a corpus
outputs the number of unique tokens 
"""


#summary statistics
#sum_stats = the_data.describe() #good summary statistics for data section
#specific stats
#avg = the_data["num_tok"].std()

#def tok_cnt(c_in):
#    return len(c_in.split())

"""
create a function that accepts a path and file name of a .txt file
and outputs the contents of the file, make sure to run it through
clean_text
"""

"""
refactor the code to NOT include any processed corpus that has 
no tokens, i.e. its blank, ie empty
"""

#cover IFs than revisit
# a = 1
# b = 4
# c = 10

# if a > 1:
#     print ("hello", a)
# elif b == 3:
#     print ("hello", b)
# elif c == 10:
#     print ("hello", c)
# elif c < 10:
#     print ("hello", c)
# else:
#     print ("Hello World")

# if a > 1:
#     print ("hello", a)
# if b == 3:
#     print ("hello", b)
# if c == 10:
#     print ("hello", c)
# if c < 10:
#     print ("hello", c)
# else:
#     print ("Hello World")






