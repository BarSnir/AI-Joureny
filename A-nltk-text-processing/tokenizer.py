import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "Hello there, how are you doing today? I hope you're doing well."

print(sent_tokenize(sentence))
print(word_tokenize(sentence))