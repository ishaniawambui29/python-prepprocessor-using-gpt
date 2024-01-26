# feature_engineer.py
from sklearn.feature_extraction.text import TfidfVectorizer

class FeatureEngineer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def engineer_features(self, texts):
        return self.vectorizer.fit_transform(texts)
