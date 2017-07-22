import nltk
from nltk.corpus import wordnet as wn
a = 'Roger is going to school. He is going to come back in evening. After that he is going to play with friends.'
b=wn.synsets('school')
print(b)

from nltk.tokenize import word_tokenize,wordpunct_tokenize, sent_tokenize

#nltk.download('punkt')

print(sent_tokenize(a))

#nltk.download('all')

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('going'))

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
words = word_tokenize('He is going to come back in evening')
print(pos_tag(words))

from nltk.stem import WordNetLemmatizer
lemmtizer = WordNetLemmatizer()
print(lemmtizer.lemmatize('going', pos='v'))

from nltk import pos_tag, ne_chunk
from nltk.tokenize import wordpunct_tokenize
c = 'Roger is going to school'
print(ne_chunk(pos_tag(wordpunct_tokenize(c))))

from nltk import word_tokenize
from nltk.util import ngrams
text = 'He is going to come back in evening'
token=nltk.word_tokenize(text)
print(ngrams(token,2))

