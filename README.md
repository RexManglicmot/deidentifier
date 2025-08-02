# 🔐 Deidentifier

**Deidentifier** is a modular Python application built with a **production-style architecture**, featuring a clean separation of logic (`app/`), logs, and tests. It detects and redacts personally identifiable information (PII) from unstructured text using [Microsoft Presidio](https://microsoft.github.io/presidio/). The system leverages advanced **Natural Language Processing (NLP)** techniques such as Named Entity Recognition (NER) and rule-based pattern matching. Evaluation is supported using standard NLP metrics like Precision, Recall, and F1 Score.

---

## 🚀 Key Features

- ✅ **Production-style architecture** with organized `app/`, `logs/`, and `tests/` directories
- 🔍 Detects PII such as **names**, **emails**, **phone numbers**, and **medical record numbers (MRNs)**
- 🧹 Redacts sensitive info using customizable regex-based and rule-based recognizers
- 📊 **Evaluation module** uses standard NLP metrics: **Precision, Recall**, and **F1 Score**
- 🪵 Structured logging with rotating file logs and console output
- 🧪 Ready for **unit testing** and **CI/CD integration**
- 💻 Easily extensible to web frameworks like **Streamlit** or **FastAPI**
