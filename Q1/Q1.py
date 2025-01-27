def counter(path):
    '''
    function to receive a text file and count how many times a word is repeated within the text
    '''
    word_count = {}
    
    with open(path, 'r') as f:
        text = f.read()
        words = text.split()
        
        for word in words:
            word = word.lower() 
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
                
    return word_count

if __name__ == "__main__":
    path = 'sample.txt'  
    counts = counter(path)
    print(counts)