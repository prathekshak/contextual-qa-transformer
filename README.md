# 🧠 Contextual QA Transformer

### AI-Powered Story Comprehension & Contextual Question Answering

**Contextual QA Transformer** is a full-stack contextual question-answering application that uses a fine-tuned **DistilBERT Transformer** to answer **Yes/No questions based on multi-sentence story contexts**.

The project demonstrates how Transformer-based NLP models can process contextual information, track relationships between entities across multiple sentences, and perform logical reasoning over a narrative.

> **Core Objective:** Use contextual Transformer-based NLP to determine whether a given statement is supported by the information contained within a story.

---

## ✨ Key Features

### 🧠 Transformer-Based Question Answering

- Fine-tuned **DistilBERT** sequence classification model
- Context-aware reasoning over multi-sentence narratives
- Story + question contextual pairing
- Binary **Yes/No** classification
- Softmax-based prediction probabilities

### 📊 Dual-Confidence Scoring

The application provides confidence scores for both possible outcomes:

```text
YES → 92%
NO  → 8%
```

This allows users to understand not only the predicted answer, but also the model's confidence in each class.

### 🎨 Interactive AI Interface

- Dark-themed UI
- Glassmorphism-inspired design
- Neon visual effects
- Responsive React interface
- Tailwind CSS styling
- Color-coded prediction results

### ⚡ Full-Stack Architecture

The application separates the presentation and inference layers:

- **React + Vite** frontend
- **FastAPI** backend
- Locally hosted Transformer model
- REST API communication
- CORS configuration for frontend/backend integration

---

# 🏗️ System Architecture

```text
┌──────────────────────────────────┐
│          React Frontend          │
│                                  │
│  Vite + Tailwind CSS             │
│  Story & Question Input          │
│  Prediction Visualization       │
└───────────────┬──────────────────┘
                │
                │ REST API
                ▼
┌──────────────────────────────────┐
│          FastAPI Backend          │
│                                  │
│  Request Validation               │
│  Model Inference                 │
│  Prediction Processing           │
└───────────────┬──────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│       DistilBERT Transformer     │
│                                  │
│  Tokenization                    │
│       ↓                          │
│  Context + Question              │
│       ↓                          │
│  Transformer Encoder             │
│       ↓                          │
│  Classification Head             │
│       ↓                          │
│  Softmax Probabilities           │
└───────────────┬──────────────────┘
                │
                ▼
       Yes / No Prediction
       + Confidence Scores
```

---

# 🧠 Model Architecture

The core NLP component uses a fine-tuned **DistilBERT sequence classification model**.

The model processes the story context and question together to determine the appropriate Yes/No classification.

### Inference Pipeline

```text
Story Context
      │
      ▼
Tokenization
      │
      ▼
Context + Question Pair
      │
      ▼
DistilBERT Transformer
      │
      ├── Self-Attention
      │
      ├── Transformer Blocks
      │
      └── Contextual Representation
               │
               ▼
       Classification Head
               │
               ▼
             Logits
               │
               ▼
      Softmax Probabilities
               │
          ┌────┴────┐
          ▼         ▼
        YES         NO
      Confidence  Confidence
```

---

## 🔍 Model Components

### 1. Tokenizer

The `DistilBertTokenizer` converts the story and question into sub-word tokens that can be processed by the Transformer.

### 2. Context-Question Pairing

The story context and question are provided as a paired input sequence, allowing the model to evaluate the question relative to the information contained in the narrative.

### 3. Transformer Encoder

DistilBERT uses **6 Transformer layers** with self-attention mechanisms to capture contextual relationships throughout the input sequence.

This allows the model to track information about entities and their state across multiple sentences.

### 4. Classification Head

The classification layer produces logits for the two possible outcomes.

These logits are converted into probabilities using **Softmax**:

```text
Logits
  │
  ▼
Softmax
  │
  ├── YES Probability
  └── NO Probability
```

---

# 🧪 Model Training

The model was trained for contextual reasoning using the **bAbI tasks**, focusing on state tracking and reasoning.

| Component | Configuration |
|---|---|
| Dataset | bAbI tasks |
| Task | State tracking & reasoning |
| Base Model | `distilbert-base-uncased` |
| Model | `DistilBertForSequenceClassification` |
| Framework | Hugging Face Transformers |
| Deep Learning Framework | TensorFlow |

---

# 📊 Prediction Example

### Input

**Story:**

```text
John picked up the football.
John went to the garden.
Mary was in the kitchen.
John left the football in the garden.
```

**Question:**

```text
Is the football in the garden?
```

### Model Output

```text
Prediction: YES

YES Confidence: 97.4%
NO Confidence: 2.6%
```

The frontend displays the prediction and confidence distribution to make the model's decision easy to interpret.

---

# 🛠️ Technology Stack

## 🤖 AI / Machine Learning

| Technology | Purpose |
|---|---|
| **DistilBERT** | Transformer-based contextual reasoning |
| **Hugging Face Transformers** | Model architecture and tokenization |
| **TensorFlow** | Model training and inference |
| **bAbI Dataset** | Story reasoning and state-tracking tasks |

## ⚙️ Backend

| Technology | Purpose |
|---|---|
| **Python 3.11** | Backend and ML runtime |
| **FastAPI** | REST API and model serving |
| **Uvicorn** | ASGI server |

## 🎨 Frontend

| Technology | Purpose |
|---|---|
| **React** | User interface |
| **Vite** | Frontend build tooling |
| **Tailwind CSS** | Styling |
| **CSS** | Custom visual effects |

---

# 📁 Project Structure

```text
contextual-qa-transformer/
│
├── backend/
│   ├── app.py
│   ├── model/
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── App.jsx
│   ├── main.jsx
│   └── ...
│
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have:

- Python 3.11+
- Node.js 16+
- npm

---

## ⚙️ Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive documentation can be accessed at:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Frontend Setup

Open a new terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The application will be available at:

```text
http://localhost:5173
```

---

# 🔄 Application Workflow

```text
1. User enters a story
          │
          ▼
2. User enters a Yes/No question
          │
          ▼
3. React sends request to FastAPI
          │
          ▼
4. DistilBERT tokenizes the input
          │
          ▼
5. Transformer processes context
          │
          ▼
6. Classification head generates logits
          │
          ▼
7. Softmax converts logits to probabilities
          │
          ▼
8. Backend returns prediction
          │
          ▼
9. React displays answer + confidence
```

---

# 💡 Technical Concepts Demonstrated

This project demonstrates practical experience with:

- Transformer architectures
- DistilBERT
- Natural Language Processing
- Contextual Question Answering
- Sequence Classification
- Self-Attention
- Tokenization
- Transfer Learning
- Fine-Tuning
- Softmax probability distributions
- FastAPI model serving
- REST API development
- React application development
- Full-stack AI application architecture

---

# 🔮 Future Improvements

Potential extensions include:

- [ ] Multi-class question answering
- [ ] Open-ended question answering
- [ ] Extractive answer highlighting
- [ ] Attention visualization
- [ ] Larger contextual windows
- [ ] Conversational memory
- [ ] Model comparison with BERT/RoBERTa
- [ ] GPU-accelerated inference
- [ ] Model performance benchmarking
- [ ] Cloud deployment
- [ ] Batch story processing

---

## 👩‍💻 Author

**Pratheksha Kanagaraj**

Computer Science Graduate Student · Software Engineer · AI/ML Enthusiast

---

⭐ **If you found this project interesting, consider giving the repository a star!**
