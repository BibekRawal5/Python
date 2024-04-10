# First, we will import TextBlob method from textblob library  
import nltk

text1 = ("Bibek, Nisha and Krishna are all living in Kathmandu.").split()  
  
# here, we will create a textblob object  
blob_object1 = nltk.pos_tag(text1)  
  
# Part-of-speech tags can be accessed through   
# the tags property of blob object.'  
  
# Now, we will print word with pos tag.  
print(blob_object1)  
