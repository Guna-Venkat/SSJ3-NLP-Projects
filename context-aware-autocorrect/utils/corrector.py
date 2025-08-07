# utils/corrector.py
import pickle
import textdistance
import pandas as pd

class AutoCorrector:
    def __init__(self, model_path='models/vocab.pkl'):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        self.vocab = model['vocab']
        self.freq = model['freq']

    def suggest(self, word, top_n=5):
        word = word.lower()
        if word in self.vocab:
            return [(word, 1.0)]  # Perfect match

        suggestions = {
            w: textdistance.jaccard(word, w) for w in self.freq.keys()
        }

        df = pd.DataFrame({
            'Word': list(suggestions.keys()),
            'Similarity': list(suggestions.values()),
            'Prob': [self.freq[w] for w in suggestions.keys()]
        })

        df = df.sort_values(by=['Similarity', 'Prob'], ascending=[False, False])
        return list(zip(df['Word'].head(top_n), df['Similarity'].head(top_n)))

    def autocorrect(self, word):
        suggestions = self.suggest(word, top_n=1)
        return suggestions[0][0] if suggestions else word
