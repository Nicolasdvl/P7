import json


class Cleaner:
    """Contain methods to clean users imputs."""

    def __init__(self):
        """Initialise."""
        self.stop_words = json.load(open("app/stopwords.json"))

    def stop_word(self, sentence: str) -> str:
        """Remove some word from a sentence given."""
        cleaned_words = []
        words = sentence.split()
        for word in words:
            if word not in self.stop_words:
                cleaned_words.append(word)
        return " ".join(cleaned_words)
