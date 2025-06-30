import os
from groq import Groq 
from dotenv import load_dotenv
 
load_dotenv()

def get_groq_client():
    return Groq(api_key=os.getenv("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"))