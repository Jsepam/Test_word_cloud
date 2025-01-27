import re
from collections import Counter

def counter(path):
    '''
    function to receive a text file and count how many times a word is repeated within the text
    but in this case it is done with a slightly more improved code since we use the collections library
    and a little regex to clean it of special characters, and delivering the word dictionary with its 
    counts and delivering the word that was in the text the most times with the most_common method 
    of the Counter class
    '''
    with open(path, 'r') as f:
        text = f.read()
        words = re.findall(r'\b\w+\b', text.lower())  
        word_count = Counter(words)  
        
    if word_count:
        highest_word = word_count.most_common(1)[0]  
    else:
        highest_word = (None, 0)  

    return dict(word_count), highest_word  

if __name__ == "__main__":
    path = 'sample.txt'
    counts, highest = counter(path)
    print("Word Counts:", counts)
    print("Highest Count Word:", highest)