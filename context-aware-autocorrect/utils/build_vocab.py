# utils/build_vocab.py
import re
import pickle
from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def build_vocab(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        
    words = re.findall(r'\w+', text)
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in words if w.isalpha() and w not in stop_words]
    
    word_freq = Counter(filtered)
    vocab = set(word_freq.keys())
    
    with open(output_path, 'wb') as f:
        pickle.dump({'vocab': vocab, 'freq': word_freq}, f)
    
    print(f"Vocabulary built and saved to {output_path}")
