from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests, os
from fastapi.responses import Response

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
ZYPHRA_KEY = os.getenv("ZYPHRA_KEY")

class Req(BaseModel):
    text: str
    voice: str = "Savannah"
    language: str = "hi"

@app.post("/v1/audio/speech")
def speak(req: Req):
    res = requests.post("https://api.zyphra.com/v1/audio/speech",
        headers={"X-API-Key": ZYPHRA_KEY, "Content-Type": "application/json"},
        json={"text": req.text, "language_iso_code": req.language, "speaking_rate": 15, "model": "zonos-v0.1-transformer", "mime_type": "audio/wav"})
    return Response(content=res.content, media_type="audio/wav")

@app.get("/")
def home():
    return {"status": "ZONOS Server Chal Raha Hai"}
