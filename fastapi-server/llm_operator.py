from openai import OpenAI
import openai
import prompts
from models import PharmacyQuestionAnswer
import json



INPUT_FILE = "01. Hypnotiká – sedatíva, anxiolytiká"
QUESTIONS_DIR = "data"


def read_chapter_and_generate_qa(topic: str, previous_questions: list[str] = []) -> PharmacyQuestionAnswer:
    with open(f"{QUESTIONS_DIR}/{topic}.json", "r", encoding="utf-8") as f:
        chapter = json.load(f)

    user_prompt = prompts.MAIN_QUESTION_USER_PROMPT.replace("{chapter_content}", chapter["content"])
    previous_questions_joined = "\n".join([f"{j+1}. {q}" for j, q in enumerate(previous_questions)])
    user_prompt = user_prompt.replace("{previous_questions_list}", previous_questions_joined)
        
    client = OpenAI()
    completion = client.chat.completions.parse(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": prompts.MAIN_QUESTION_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=1000,
        response_format=PharmacyQuestionAnswer
    )

    content: PharmacyQuestionAnswer = completion.choices[0].message.parsed
    return content


