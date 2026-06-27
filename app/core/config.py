from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OUTPUT_DIR = "outputs"
TEMPLATE_DIR = "templates"