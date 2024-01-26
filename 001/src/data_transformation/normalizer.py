# normalizer.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class DataNormalizer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def normalize(self, texts):
        normalized_texts = []
        for text in texts:
            words = word_tokenize(text)
            lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words if word.isalpha() and word not in self.stop_words]
            normalized_text = ' '.join(lemmatized_words)
            normalized_texts.append(normalized_text)
        return normalized_texts
