import random 
import os
import string
import sys

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"
        

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = []
    # TODO
    import re
    
    regex_delimiters = "[\t,;\.\?\!\-\:@\[\]\(\)\{\}_\*/]+"
    lines = sys.stdin.readlines()
    certain_lines = [lines[idx] for idx in indexes]
    word_count = {} # a dictionary to store frequencies of all words
    for line in certain_lines:
        line = re.sub('\n', '', line) # get rid of \n at the end of each line
        line = line.strip()
        sep_line = re.split(regex_delimiters, line) # Divide each sentence into a list of words using delimiters
        sep_line = [i.lower() for i in sep_line] # make all tokens lower case
        
        sep_line = [i for i in sep_line if i]  # remove empty string from the list
        
        
        # remove word from stopWordsList and counting each word's frequency
        for word in sep_line:
            if word not in stopWordsList:
                if word in word_count:
                   word_count[word] += 1
                else:
                    word_count[word] = 1
        
    
    # sorting words in descending and Lexicographical order
    word_sort = sorted(word_count.items(), key=lambda x:(-x[1], x[0]))
    
    # add the top 20 words in the ret
    for i in range(20):
        ret.append(word_sort[i])
                
    for word in ret:
        print(word[0])

process(sys.argv[1])
