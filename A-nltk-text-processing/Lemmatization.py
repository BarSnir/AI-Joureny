connect_tokens = ['connecting', 'connected', 'connectivity', 'connect', 'connects']
learn_tokens = ['learned', 'learning', 'learn', 'learns', 'learner', 'learners']
likes_tokens = ['likes', 'better', 'worse']

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
for t in connect_tokens:
    print(t, " : ", lemmatizer.lemmatize(t))
for t in learn_tokens:
    print(t, " : ", lemmatizer.lemmatize(t))
for t in likes_tokens:
    print(t, " : ", lemmatizer.lemmatize(t))