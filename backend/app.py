from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import TFDistilBertForSequenceClassification, DistilBertTokenizer
import tensorflow as tf

app = FastAPI(title="NeuroQA - Transformer API")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "./transformer_model"
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = TFDistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

class QueryRequest(BaseModel):
    story: str
    question: str

@app.get("/")
def home():
    return {"status": "NeuroQA Backend is Online"}

@app.post("/predict")
async def predict(request: QueryRequest):
    try:
        input_text = f"{request.story} [SEP] {request.question}"
        inputs = tokenizer(input_text, return_tensors="tf", padding=True, truncation=True)
        
        outputs = model(inputs)
        logits = outputs.logits
        probabilities = tf.nn.softmax(logits, axis=-1).numpy()[0]
        
        prediction_idx = int(tf.argmax(logits, axis=-1).numpy()[0])
        answer = "Yes" if prediction_idx == 1 else "No"
        return {
            "answer": answer,
            "confidence_yes": float(probabilities[1]),
            "confidence_no": float(probabilities[0]),
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)