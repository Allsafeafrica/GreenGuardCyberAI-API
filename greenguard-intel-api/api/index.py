# api/index.py

from fastapi import FastAPI
from datasets import load_dataset

app = FastAPI()

# Load Hugging Face dataset (stream=False for full local load)
dataset = load_dataset("Allsafeafrica/GreenGuard-Intel-Base")['train']

@app.get("/")
def home():
    return {"msg": "Welcome to GreenGuard Intel API 🌿"}

@app.get("/insights/latest")
def latest_entry():
    return dataset[-1]

@app.get("/insights/{index}")
def get_entry(index: int):
    if 0 <= index < len(dataset):
        return dataset[index]
    return {"error": "Index out of range"}

@app.get("/insights")
def all_data(limit: int = 10):
    return dataset[:limit]
