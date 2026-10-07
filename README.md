# 🧠 NeuroQA – Story Comprehension Bot

## AI-Powered Contextual Question Answering (Full-Stack)

NeuroQA is a full-stack web application designed to demonstrate contextual question answering (CQA) using a modern **Transformer-based Neural Network**. The application allows a user to input a multi-sentence "story" (context) and a "Yes/No" question, and the backend model determines the logical answer based on the provided narrative.

## ✨ Features

* **Premium Frontend:** Features a high-contrast **Dark, Glassy, and Neon-Glow** UI built with React and Tailwind CSS.
* **Transformer Model (DistilBERT):** Utilizes a fine-tuned `DistilBertForSequenceClassification` model for superior logical reasoning and state tracking.
* **Full-Stack Architecture:** Separated Frontend (React/Vite) and Backend (FastAPI) with optimized CORS handling.
* **Dual-Confidence Scoring:** Provides real-time reliability percentages for both 'Yes' and 'No' outcomes using Softmax probability distributions.

## 🏛️ Architecture Overview

The project is split into two main directories:

| Directory | Technology | Role |
| :--- | :--- | :--- |
| `frontend/` | React (Vite) & Tailwind CSS | Handles user input, displays the prediction result, and provides the premium Neon UI. |
| `backend/` | Python (FastAPI) & TensorFlow | Serves predictions via a REST API, utilizing a locally hosted Transformer model. |

---

## ⚙️ Core ML Component Details

This section details the design and implementation of the machine learning model.

### 🧠 Model Architecture

The chatbot uses a **Transformer (DistilBERT)** architecture, which understand the relationship between different parts of a story.



1.  **Tokenizer:** Uses `DistilBertTokenizer` to process input text into sub-word tokens.
2.  **Context-Question Pairing:** The story and question are merged using the `[SEP]` (separator) token to create a single input sequence.
3.  **Self-Attention Layers:** 6 layers of Transformer blocks allow the model to track the "state" of objects and people across multiple sentences.
4.  **Classification Head:** A final dense layer outputs **Logits**, which are converted to probabilities via **Softmax** to determine the final "Yes" or "No" answer.

### 🛠️ Model Training

* **Dataset:** bAbI tasks (State tracking and reasoning).
* **Base Model:** Pre-trained `distilbert-base-uncased`.
* **Framework:** Hugging Face Transformers + TensorFlow.

---

## 🛠️ Setup and Installation

### Prerequisites

* **Python (3.11.7)**
* **Node.js (16+) & npm**

### 1. Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Backend API:**
    ```bash
    uvicorn app:app --reload
    ```
    The API should now be running at `http://127.0.0.1:8000`.

### 2. Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```
2.  **Install Node dependencies:**
    ```bash
    npm install
    ```
3.  **Run the Frontend Development Server:**
    ```bash
    npm run dev
    ```
    The web application should open in your browser at `http://localhost:5173`.

## 🚀 How to Use

1.  Ensure both the **Backend API** (port 8000) and the **Frontend App** (port 5173) are running.
2.  Input a multi-sentence **Story Context** and a **Yes/No Question**.
3.  Click **'Get Answer'**. The model's prediction and color-coded confidence score will update instantly.

---
