from nltk.tokenize import sent_tokenize, word_tokenize
  
text = "Hello World. How's the weather today ? We here at Bhaktapur. It's too cold"
sentence_tokens=sent_tokenize(text)
print("SENTENCE TOKENIZATION: ", sentence_tokens)

word_tokens=word_tokenize(text)
print("WORD TOKENIZATION: ", word_tokens)