# cleaner.py
import re

class DataCleaner:
    def clean(self, texts):
        cleaned_texts = []
        for text in texts:
            if text:
                text = text.lower()
                text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
                text = re.sub(r'[^\w\s]', '', text)  # remove special characters
                cleaned_texts.append(text)
        return cleaned_texts
