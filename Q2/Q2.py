import re
from collections import Counter

def counter(path):
    '''
    function to receive a text file and count how many times a word is repeated within the text
    but in this case it is done with a slightly more improved code since we use the collections library
    and a little regex to clean it of special characters, Using the sorted function to give it 
    a bit of order and generate the result from highest to lowest
    '''
    with open(path, 'r') as f:
        text = f.read()
        words = re.findall(r'\b\w+\b', text.lower())  
        word_count = Counter(words)  
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))    
    return dict(sorted_word_count)  

if __name__ == "__main__":
    path = 'sample.txt'
    counts = counter(path)
    print(counts)