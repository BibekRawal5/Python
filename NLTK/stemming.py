# import these modules
from nltk.stem import PorterStemmer
 
ps = PorterStemmer()
 
# choose some words to be stemmed
words = ["studies", "studious"]
 
for w in words:
    print(w, " : ", ps.stem(w))