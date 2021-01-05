import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')

#NO USE (Will remove later)
#def tokenCreation(content):
    #tokenContent = nltk.sent_tokenize(content)
    #return tokenContent

def corpus(tokenConent):
    CORPUS = []
    for i in range(len(tokenConent)):
        review = re.sub('\n',' ',str(tokenConent[i]))
        review = review.lower()
        review = review.split()
        review = ' '.join(review)
        CORPUS.append(review)
      
    return CORPUS

