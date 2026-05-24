import re

with open("the-verdict.txt", "r") as f:
    raw_text = f.read()

"""
print("Total no. of Characters are ",len(raw_text)) #Prints total number of characters
print(raw_text[:99]) #Prints first 100 characters for illustration purpose
# Our goal is to tokenize all the individual words and special characters trhat we can turn into embeddings for LLM training.

#BASIC TOKENIZATION PROCESS
# STEP 1: First split the data according to the words and special characters
# STEP 2: Remove the white spaces
"""
#STEP 1 (Tokenizing the short story)
preprocessed = re.split(r'([,.:;?_!""()\']|--|\s)',raw_text)
preprocessed = [item for item in preprocessed if item.split()]
#print(preprocessed[:30])
#print(len(preprocessed))


#STEP 2 (Token ID)

#Create a list of all unique tokens to see the vocabulary size

all_words = sorted(set(preprocessed))
vocal_size = len(all_words)

print(vocal_size)

#Now we create the vocabulary (Tokens and Token IDs)

vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break