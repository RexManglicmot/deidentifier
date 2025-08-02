![Project Status](https://img.shields.io/badge/status-actively--developed-yellowgreen)

# 🛠️ Status

This project is **currently** being developed and improved with additional features and testing.


# 🔐 Deidentifier

**Deidentifier** is a Python application built with a **production-style code architecture**, featuring a clean separation of directories such as `app/`, `logs/`, and `tests/` seen in industries practices. Deidentifier detects and redacts personally identifiable information (PII) from unstructured text using [Microsoft Presidio](https://microsoft.github.io/presidio/) that leverages advanced **Natural Language Processing (NLP)** techniques such as Named Entity Recognition (NER) and rule-based pattern matching. Evaluation is supported using standard NLP metrics like Precision, Recall, and F1 Score.



## 🚀 Key Features

- ✅ **Production-style code architecture** with organized `app/`, `logs/`, and `tests/` directories
- 🔍 Detects PII such as **names**, **emails**, **phone numbers**, and **medical record numbers (MRNs)**
- 🧹 Redacts sensitive info using customizable regex-based and rule-based recognizers
- 📊 **Evaluation module** uses standard NLP metrics: **Precision, Recall**, and **F1 Score**
- 🪵 Structured logging with rotating file logs and console output
- 🧪 Ready for **unit testing** and **CI/CD integration**
- 💻 Easily extensible to web frameworks like **Streamlit** or **FastAPI**


## 🛠️ Tech Stack  
- Python · Microsoft Presidio · Streamlit · FastAPI  
- logging · pytest · GitHub Actions · Docker  