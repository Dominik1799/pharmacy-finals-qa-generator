from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import llm_operator
from models import PharmacyQuestionAnswer
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/")
async def generate_pharmacy_qa(topic: str = Query(default=llm_operator.INPUT_FILE), previous_questions: list[str] = Query(default=[])) -> PharmacyQuestionAnswer:
	return llm_operator.read_chapter_and_generate_qa(topic, previous_questions)
