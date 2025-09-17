from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import llm_operator
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import PharmacyQuestionAnswer
import os
import settings
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/api/generate_pharmacy_qa", response_model=PharmacyQuestionAnswer)
async def generate_pharmacy_qa(topic: str = Query(default=llm_operator.INPUT_FILE), previous_questions: list[str] = Query(default=[])) -> PharmacyQuestionAnswer:
	return llm_operator.read_chapter_and_generate_qa(topic, previous_questions)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # list files in data directory and remove .json suffix
    files = os.listdir(settings.PARSED_QUESTIONS_DIRECTORY)
    topics = [f[:-5] for f in files if f.endswith(".json")]
    topics.sort()
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request, "topics": topics})


@app.get("/topic/{topic}", response_class=HTMLResponse)
async def index(request: Request, topic: str):

    return templates.TemplateResponse(request=request, name="topic.html", context={"request": request, "topic": topic})
