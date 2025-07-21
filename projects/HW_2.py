#!/usr/bin/env python3
"""
Homework 2 | Natural Language Processing for the Social Sciences (GR5067)

"""
import os
NAME = "Philip Auerbach" 
UNI = "PJA2113"  

def file_crawler(p_in):
    import pandas as pd
    import os
    tmp_d = pd.DataFrame()
    for root, dirs, files in os.walk(p_in, topdown=False):
       for name in files:
            if not name.lower().endswith(".txt"):
                continue  # skip non-text files
            tmp = os.path.join(root, name)
            t_txt = file_opener(tmp)
            if len(t_txt) != 0:
            #if t_txt is not None:  
              t_dir = root.split("/")[-1]
              tmp_pd = pd.DataFrame(
                  {"body": t_txt, "label": t_dir}, index=[0])
              tmp_d = pd.concat([tmp_d, tmp_pd], ignore_index=True)
    return tmp_d



def gen_senti(corpus):
    import os
    import string
    base_dir = os.path.dirname(os.path.abspath(__file__))

    negative_path = os.path.join(base_dir, 'negative-words.txt')
    positive_path = os.path.join(base_dir, 'positive-words.txt')

    positive_set = set()
    negative_set = set()
    with open(negative_path, 'r', encoding='ISO-8859-1') as file:
        for line in file: 
            negative_set.add(line.strip())
        
    with open(positive_path, 'r', encoding='ISO-8859-1') as file:
        for line in file: 
            positive_set.add(line.strip())


    #Postive Count 
    pc = 0
    #Negative Count 
    nc = 0
    #Sentiment Score 
    sc = 0
    #Token Corpus 
    for word in corpus.split():
        clean_word = word.lower().strip(string.punctuation)
        if clean_word in positive_set:
            print(f"POSITIVE: {clean_word}")
            pc += 1
            sc += 1
        elif clean_word in negative_set:
            print(f"NEGATIVE: {clean_word}")
            nc += 1
            sc -= 1

    if pc + nc == 0:
        return 0    
    sc = sc/(pc+nc)
    
    return sc 

the_d_path = "/Users/philipauerbach/Desktop/git projects/NLP-SS Class/NLP-SS/git/data/course_data"
the_data = file_crawler(the_d_path)

the_data.head(5)
"""
2.	 Using the dataframe from lecture, the_data, column body, apply this function to each corpus and add a column called “simple_senti” (15 points)

3.	Using vaderSentiment, apply the “compound” value of sentiment for each corpus in column body on a new column of the_data called “vader” (15 points)

4.	Compute the mean, median and standard_deviations of both sentiment measures, “simple_senti” and “vader”  (10 points)


"""