import os
import json
import PyPDF2
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key = API_KEY)


def read_resume(uploaded_file):
    text = ""

    reader = PyPDF2.PdfReader(uploaded_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def analyze_resume(resume_text, prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert ATS Resume Analyzer."
            },
            {
                "role": "user",
                "content": prompt + resume_text
            }
        ],
        temperature=0.2
    )

    result = response.choices[0].message.content

    try:
        return json.loads(result)
    except:
        return {"response": result}