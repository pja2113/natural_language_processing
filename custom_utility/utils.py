# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 18:09:29 2025

@author: Philip Auerbach
"""
# NLP RELEVANT FUNCTIONS 

# Function: Jaccard Similarity (String)
# Purpose:  Measure of how similar two strings are
# Input: Two strings to compare similarity
# Output: float - score between 0 and 1 (inclusive)

def jd_sim_string(str_a, str_b):
    tok_a = str_a.split()
    tok_b = str_b.split()
    set_a = set(tok_a)
    set_b = set(tok_b)
    inter_tmp = set_a.intersection(set_b)
    union_tmp = set_a.union(set_b)
    jd_tmp = len(inter_tmp) / len(union_tmp)
    return jd_tmp

# Function: Adder
# Purpose:  Add two values with basic error handling
# Input: Two values to add (a_in, b_in)
# Output: Sum if successful, else None

def adder(a_in, b_in):
    tmp = None
    try:
        tmp = a_in + b_in
    except:
        print ("can't add", a_in, b_in)
        pass
    return tmp

# Function: Word Frequency
# Purpose:  Count frequency of words in a string
# Input: A string
# Output: Dictionary of word counts

def wrd_freq(c_in):
    tmp = c_in.split()
    t_d = dict()
    for word in set(tmp):
        t_d[word] = tmp.count(word)
    return t_d


# Function: Word Frequency (Redux)
# Purpose:  Efficiently count frequency of words in a string
# Input: A string
# Output: Dictionary of word counts

def wrd_freq_redux(str_in):
    import collections
    the_new_ans = dict(collections.Counter(str_in.split()))
    return the_new_ans

# Function: Clean Text
# Purpose:  Remove non-letter characters, lowercase text
# Input: A string
# Output: Cleaned string

def clean_text(str_in):
    import re
    cln_txt = re.sub(
        "[^A-Za-z']+", " ", str_in).strip().lower()
    return cln_txt

# Function: File Opener
# Purpose:  Open a file, read and clean its contents
# Input: File path as a string
# Output: Cleaned text from file or empty string on failure

def file_opener(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return clean_text(f.read())
    except Exception as e:
        print("Can't open", file_path, "→", e)
        return ''

# Function: File Crawler
# Purpose:  Recursively read and label text files in a directory
# Input: Directory path
# Output: Pandas DataFrame with 'body' and 'label' columns

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

# Function: Token Counter
# Purpose:  Count total or unique tokens in text
# Input: Text string, mode ("all" or anything else for unique)
# Output: Integer token count

def tok_cnt(c_in, sw_in):
    tmp = c_in.split()
    if sw_in == "all":
        return len(tmp)
    else:
        return len(set(tmp))

# Function: Word Statistics
# Purpose:  Compute total and unique token counts by topic
# Input: DataFrame with 'label' and 'body' columns
# Output: Dictionary with counts for each topic

def wrd_fun(df_in):
    combined_t = dict()
    for topic in df_in["label"].unique():
        tmp = df_in[df_in["label"] == topic]
        tmp = tmp["body"].str.cat(sep= " ")
        tmp = tmp.split()
        tmp_all = len(tmp)
        tmp_u = len(set(tmp))
        combined_t[topic] = {"all": tmp_all, "unique": tmp_u}
        # combined = the_data.groupby('label', as_index=False).agg({'body': ' '.join})
        # combined['num_token'] = combined['body'].apply(lambda x: tok_cnt(x,"all"))
        # combined['num_token_unique'] = combined['body'].apply(lambda x: tok_cnt(x,"u"))
        # result_dict = {}
        # for _,row in combined.iterrows():
        #     result_dict[row['label']] = {
        #         'all': row['num_token'],
        #         'unique': row['num_token_unique']
        #     }
    return combined_t


# Function: Remove Stopwords
# Purpose:  Remove English stopwords from a string
# Input: A string
# Output: Cleaned string with stopwords removed
    
def rem_sw(text):
    
    from nltk.corpus import stopwords
    sw = stopwords.words('english')
    return ' '.join([word for word in text.split() if word.lower() not in sw])

# Function: Word Stemming
# Purpose:  Reduce each word in a string to its root form 
# Input: A string 
# Output: A string will all words stemmed 

def stem_fun(str_input):
    from nltk.stem import PorterStemmer 
    ps = PorterStemmer()
    tmp = str_input.split()
    stemmed_words = [ps.stem(word) for word in tmp]
    return ' '.join(stemmed_words)

# Function: Word Counter by Topic
# Purpose:  Count individual word occurrences by topic
# Input: DataFrame with 'label' and 'body' columns
# Output: Dictionary of word Counter objects per topic

def word_fun(df_in):
    import collections
    wrd_cnt_fun = dict()
    for topic in df_in["label"].unique():
        tmp = df_in[df_in["label"] == topic]
        tmp = tmp["body"].str.cat(sep=" ")
        wrd_cnt_fun[topic] = collections.Counter(tmp.split())
    return wrd_cnt_fun

# Function: lemma_fun
# Purpose:  Perform basic lemmatization on a string of text.
# Input:    str_corpus - a string containing the input text (sentence or document)
# Output:   A new string with each word reduced to its lemma (base form)


def lemma_fun(str_corpus):
    from nltk.stem import WordNetLemmatizer
    wnl = WordNetLemmatizer()
    tmp = str_corpus.split()
    lemmatized_corpus = [wnl.lemmatize(word)for word in tmp]
    return ' '.join(lemmatized_corpus)

# Function: stem_fun
# Purpose:  Perform stemming or lemmatization on a given text string based on the selected method.
# Input:    
#   - str_corpus (str): The input text (sentence or document).
#   - flag (str): 
#         -'ps'  → Porter Stemmer (rule-based stemming)
#         -'wnl' → WordNet Lemmatizer (dictionary-based lemmatization)
# Output:   
#   - A processed string where each word has been stemmed or lemmatized.
#   - If an invalid flag is passed, prints an error message and returns None.

def stem_fun(str_corpus, flag):
    from nltk.stem import WordNetLemmatizer, PorterStemmer

    if flag == "ps":
        ps = PorterStemmer()
        tmp = str_corpus.split()
        stemmed_words = [ps.stem(word) for word in tmp]
        return ' '.join(stemmed_words)
    
    elif flag == "wnl":
        wnl = WordNetLemmatizer()
        tmp = str_corpus.split()
        lemmatized_corpus = [wnl.lemmatize(word)for word in tmp]
        return ' '.join(lemmatized_corpus)
    
    else: 
        print("Error: Please provide a valid flag — 'ps' for PorterStemmer or 'wnl' for WordNetLemmatizer.")
        return None

# Function: read_pickle
# Input: path and filename
# Output: loaded object from pickle file
def read_pickle(path_in, name_in):
    import pickle
    the_data_t = pickle.load(open(path_in + name_in + ".pk", "rb"))
    return the_data_t

# Function: write_pickle
# Input: object, path, and filename
# Output: saves object to pickle file
def write_pickle(obj_in, path_in, name_in):
    import pickle
    pickle.dump(obj_in, open(path_in + name_in + ".pk", "wb"))


# ALTERNATIVE EFFICIENCY FUNCTIONS 

# def rem_sw(str_in):
#     n_l = list()
#     from nltk.corpus import stopwords
#     sw = stopwords.words('english')
#     # n_l = [word for word in t_c.split() if word not in sw]
#     # n_l = " ".join(n_l)
#     for word in str_in.split():
#         if word not in sw:
#             n_l.append(word)
#     n_l = " ".join(n_l)
#     return n_l

# def file_opener(p_in):
#     try:
#         txt = ''
#         #txt = None
#         f = open(p_in, "r", encoding="UTF8")
#         txt = f.read()
#         txt = clean_text(txt)
#         f.close()
#     except:
#         print ("Can't open", p_in)
#         pass
#     return txt