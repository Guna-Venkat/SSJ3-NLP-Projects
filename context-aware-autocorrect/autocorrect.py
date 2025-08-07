# autocorrect.py

import nltk
import difflib
import re
import string

# Download once
try:
    nltk.data.find("corpora/words")
except LookupError:
    nltk.download("words")

from nltk.corpus import words

class SimpleSpellCorrector:
    def __init__(self):
        self.vocab = set(w.lower() for w in words.words())
        self.punctuation = set(string.punctuation)

    def is_valid_word(self, word):
        return word.lower() in self.vocab

    def get_closest_match(self, word):
        if self.is_valid_word(word):
            return word
        suggestions = difflib.get_close_matches(word.lower(), self.vocab, n=1, cutoff=0.8)
        return suggestions[0] if suggestions else word

    def clean_text(self, text):
        # Normalize spaces and remove unusual punctuation (except periods)
        return re.sub(r"[^\w\s\.\']", '', text.lower().strip())

    def correct_sentence(self, sentence):
        sentence = self.clean_text(sentence)
        words = sentence.split()
        corrected_words = [self.get_closest_match(w) for w in words]
        return " ".join(corrected_words)

a = SimpleSpellCorrector()
print(a.correct_sentence('Writng code iz fun and educatinal.'))