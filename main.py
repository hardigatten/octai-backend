from fastapi import FastAPI, UploadFile, File
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/analyze-oct/")
async def analyze_oct(file: UploadFile = File(...)):
    od_diag = "Contorni foveali regolari"
    os_diag = "Sollevamento dell’epitelio pigmentato retinico"

    prompt = f"""Fornisci un referto OCT sintetico nel formato:
OCT Macula
OD: {od_diag}
OS: {os_diag}
Nota: Scrivi solo se necessaria una nota, in una riga."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=150
    )

    return {"output": response.choices[0].message.content}
