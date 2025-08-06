# ✍️ AutoCorrect NLP — Context-Aware Spell Correction Engine

<p align="center">
  <a href="https://gradio.app/">
    <img src="https://img.shields.io/badge/Gradio-UI_Framework-blue?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio UI"/>
  </a>
  <a href="https://www.nltk.org/">
    <img src="https://img.shields.io/badge/NLTK-Core_NLP_Tools-green?style=for-the-badge&logo=python&logoColor=white" alt="NLTK NLP Tools"/>
  </a>
</p>

This repository features a **modular, context-aware spell correction system** that simulates how modern editors (like Gmail, Notion, or smartphone keyboards) detect and fix spelling mistakes in **real-time**. The project leverages traditional NLP methods like **Levenshtein Distance**, **language modeling**, and **embedding-based similarity** for context-sensitive suggestions.

It is designed for foundational learning in **Natural Language Processing (NLP)**.

---

## 🎯 Objective

- 🔤 Build a token-based autocorrector using NLP
- 🛠️ Learn Levenshtein Distance and dictionary-based spell correction
- 📊 Train a context-based language model (n-gram)
- 🧠 Improve with semantic correction using embeddings
- 🧪 Deploy via **Gradio** interface for real-time correction

---

## 📁 Features

| Component               | Tech Stack              |
|------------------------|-------------------------|
| Tokenization           | `NLTK`                  |
| Edit Distance          | `Levenshtein` (custom)  |
| Dictionary             | `nltk.corpus.words`     |
| Corpus                 | `Wikipedia` (NLTK)      |
| Language Model         | `N-gram`                |
| Embedding Similarity   | `GloVe` or `FastText`   |
| UI                     | `Gradio`                |

---

## 🧭 Workflow

### ✅ AutoCorrect Pipeline

| Step | Description |
|------|-------------|
| 🧹 Preprocessing | Clean and tokenize input sentence |
| 🧮 Edit Distance | Generate candidate corrections (Levenshtein) |
| 📚 Word Lookup | Filter words using NLTK dictionary |
| 📊 Rank by Frequency | Use corpus frequency from Wikipedia |
| 📈 Context-Aware Model | Apply N-gram scoring |
| 🧠 Embedding-Based Correction | Use semantic similarity |
| 🤖 Final Suggestion | Return corrected sentence through UI |

---

## 🧰 Installation Guide

### ✅ Python Environment

```bash
python -m venv autocorrect_env
source autocorrect_env/bin/activate  # On Windows: autocorrect_env\Scripts\activate
```

### ✅ Install Python Dependencies

```bash
pip install nltk gradio numpy pandas tqdm
python -m nltk.downloader punkt words brown reuters
```

### 🚀 How to Run
```bash
python interface.py
```

### 🚀 How to Use

---

After Running the App

- ✍️ **Type a sentence** with spelling errors
- ✅ **View auto-corrected version** based on context
- 🔁 **Try with different models** (edit-only vs context-aware)
- 📊 **Switch to semantic correction** for more intelligent suggestions

---

## 📊 Visualizations

| Feature               | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| 🧠 **Context-Aware Flow** | Shows which model corrected each word                        |
| 📈 **Correction Log**     | Tracks which words were edited and why                       |
| 🖼️ **UI Screenshots**     | Interface view of deployed Gradio application                |

<p align="center"> 
  <img src="deployed_app_img1.PNG" alt="Deployed App Screenshot 1" width="600"/>
</p>
<p align="center"> 
  <img src="deployed_app_img2.PNG" alt="Deployed App Screenshot 2" width="600"/>
</p>

---

## 📦 Folder Structure

```bash
context-aware-autocorrect/
├── autocorrect.py             # Core logic (functions for LM, edit distance, etc.)
├── interface.py               # Gradio-based frontend
├── demo.ipynb                 # Notebook for testing & evaluation
├── README.md                  # This file
├── data/                      # Corpus and dictionary files
├── models/                    # Trained LM or word embeddings
```

## 🧾 Sample Usage

```bash
Input1:  "Ths is a smple txt with erors"
Output1: "This is a simple text with errors"

Input2:  "I am planing to goo to thee markit"
Output2: "I am planning to go to the market"
```

## 🧠 Future Work

- ⌨️ Add real-time keyboard integration  
- 🤖 Build Transformer-based corrector (e.g., BERT Masking)  
- 🌍 Add support for multilingual dictionaries  
- 🔍 Integrate with search/autocomplete engines  

---

## 📚 Learnings

- 🧱 How classic NLP methods (Edit Distance, Frequency, N-grams) still power real-world features  
- 🔁 Combining rule-based and data-driven models leads to better accuracy  
- 🧠 Context-aware embeddings significantly improve suggestions  
- ⚡ Gradio enables rapid prototyping of NLP tools with minimal setup  

---

## ✍️ Author

**Name**: Guna Venkat Doddi  
**Project**: Part of `SSJ3-AI-Agent-Projects`  
**Contact**: [LinkedIn/GitHub/Email – Add here if you want]  
