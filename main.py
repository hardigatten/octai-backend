{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ffrom fastapi import FastAPI, UploadFile, File\
import openai\
import os\
\
app = FastAPI()\
\
openai.api_key = os.getenv("OPENAI_API_KEY")\
\
@app.post("/analyze-oct/")\
async def analyze_oct(file: UploadFile = File(...)):\
    # Dati simulati per prototipo\
    od_diag = "Contorni foveali conservati, nessun fluido."\
    os_diag = "Disorganizzazione strati interni, sollevamento RPE."\
\
    prompt = f"""Fornisci un referto OCT sintetico in italiano nel formato:\
OCT Macula\
OD: \{od_diag\}\
OS: \{os_diag\}\
Nota: Scrivi una frase breve solo se necessario."""\
\
    response = openai.ChatCompletion.create(\
        model="gpt-4",\
        messages=[\{"role": "user", "content": prompt\}],\
        temperature=0.3,\
        max_tokens=200\
    )\
\
    return \{"output": response["choices"][0]["message"]["content"]\}}