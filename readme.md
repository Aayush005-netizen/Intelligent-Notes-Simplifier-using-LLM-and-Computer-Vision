## 👥 Team

> Building an AI-powered Notes Simplification System using Deep Learning, NLP, Computer Vision, and FastAPI.

---

### 🚀 Aayush Dubey

**Role:** AI Engineer & Backend Developer

#### Responsibilities
- 🔹 Backend Development with FastAPI
- 🔹 Deep Learning & PyTorch Integration
- 🔹 Keyword Extraction Pipeline (TF-IDF, KeyBERT)
- 🔹 System Architecture & API Design
- 🔹 Deployment & Infrastructure

---

### 🚀 Nikhil Jha

**Role:** NLP & Computer Vision Engineer

#### Responsibilities
- 🔹 NLP Model Development & Research
- 🔹 Text Summarization Pipeline (BART/T5)
- 🔹 OCR & Computer Vision Integration
- 🔹 Model Evaluation & Optimization
- 🔹 Testing & Performance Analysis

---

### 🤝 Collaboration

Both team members actively contribute to:

- ✅ Project Planning
- ✅ System Design & Architecture
- ✅ Feature Development
- ✅ Testing & Debugging
- ✅ Documentation
- ✅ Deployment & Maintenance

---

### 🎯 Project Goal

Develop a complete **AI-powered Notes Simplification Platform** capable of:

- 📝 Summarizing Notes
- 🔑 Extracting Keywords
- ❓ Answering Questions
- 📚 Generating Flashcards
- 🖼️ Processing Images via OCR
- 📄 Handling PDF & DOCX Documents

---

> *Learning by building, experimenting, and deploying real-world AI systems.*

Both team members actively contribute to project planning, architecture design, implementation, testing, debugging, documentation, and deployment. The project follows a collaborative development workflow, ensuring hands-on experience across NLP, Computer Vision, Deep Learning, Backend Engineering, and MLOps while building a complete end-to-end AI-powered Notes Simplification System.

---

## Project WorkFlow
```mermaid
flowchart TB

    subgraph Input Layer
        A1[Text]
        A2[PDF]
        A3[DOCX]
        A4[Image]
    end

    subgraph Processing Layer
        B1[PDF Parser]
        B2[DOCX Parser]
        B3[ResNet Classifier]
        B4[OCR Engine]
        B5[Text Cleaner]
    end

    subgraph AI Layer
        C1[BART Summarizer]
        C2[KeyBERT Extractor]
        C3[Question Answering]
        C4[Flashcard Generator]
    end

    subgraph API Layer
        D1[FastAPI Backend]
    end

    subgraph Output Layer
        E1[Summary]
        E2[Keywords]
        E3[Q&A]
        E4[Flashcards]
    end

    A1 --> B5
    A2 --> B1
    A3 --> B2
    A4 --> B3

    B1 --> B5
    B2 --> B5
    B3 --> B4
    B4 --> B5

    B5 --> C1
    C1 --> C2
    C2 --> C3
    C3 --> C4

    C4 --> D1

    D1 --> E1
    D1 --> E2
    D1 --> E3
    D1 --> E4

```