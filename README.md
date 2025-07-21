# Natural Language Processing
This repository contains Natural Language Processing (NLP) projects and a comprehensive utility library for text processing and analysis.

## Install
These projects utilize and require downloading Python and NLTK data

Code for NLTK download:
```python
# Python Kernel
import nltk
nltk.download()
# GUI opens, download all.
```

## Project Files

## Core Files
**custom_utility/utils.py** - Comprehensive NLP utility library containing functions for:
- Text similarity (Jaccard similarity)
- Text cleaning and preprocessing
- File I/O operations for text data
- Token counting and word frequency analysis
- Stopword removal
- Stemming and lemmatization
- Data serialization (pickle operations)

**lectures.py** - Main processing script that:
- Loads and processes course data from `/data/course_data`
- Applies NLP transformations (tokenization, stopword removal, stemming)
- Generates word frequency statistics
- Demonstrates usage of utility functions

## Utility Functions Overview
The `custom_utility/utils.py` library includes:

#### Text Processing
- `clean_text()` - Remove non-letter characters and normalize text
- `rem_sw()` - Remove English stopwords
- `stem_fun()` - Porter stemming with optional lemmatization
- `lemma_fun()` - WordNet lemmatization

#### Analysis Functions
- `jd_sim_string()` - Calculate Jaccard similarity between strings
- `tok_cnt()` - Count total or unique tokens
- `wrd_freq()` / `wrd_freq_redux()` - Word frequency counting
- `wrd_fun()` - Token statistics by topic/label
- `word_fun()` - Individual word occurrence counting by topic

#### File Operations
- `file_opener()` - Read and clean text files
- `file_crawler()` - Recursively process text files in directories
- `read_pickle()` / `write_pickle()` - Data serialization

### Other Files
**HW_1.py** - Basic Python functionality exercises
**/data** - Datasets used across all projects
**/outputs** - Output folder for function results and project datasheets



