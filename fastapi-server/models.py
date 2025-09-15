from pydantic import BaseModel



class PharmacyQuestionAnswer(BaseModel):
    question: str
    answer: str


