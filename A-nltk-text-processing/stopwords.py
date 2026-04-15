import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


he_stopwords = stopwords.words('hebrew')
print(he_stopwords)