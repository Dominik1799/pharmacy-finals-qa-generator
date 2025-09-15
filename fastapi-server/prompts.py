MAIN_QUESTION_SYSTEM_PROMPT = """
Generate a single, new exam-preparation question and answer in Slovak based strictly on the provided markdown content of a college-level pharmacy textbook chapter, ensuring that the question is clearly distinct from all previous questions in the supplied list.


Your task:

- Carefully read and understand the provided chapter content.
- Analyze key points, major concepts, and important facts suitable for examination or knowledge assessment.
- Review the list of previously generated questions and ensure your new question is different (not too similar in topic, wording, or focus) and contributes to diversity in assessment.
- Devise one thoughtful and clear exam-style question in Slovak that tests understanding of a major topic presented in the chapter. Use open-ended or short-answer formats; avoid true/false or purely factual recall if possible.
- Provide a correct, concise, and academically phrased answer in Slovak—synthesizing the most relevant information from the chapter.
- Both question and answer must be college-level, academically appropriate, and based strictly on the provided chapter content.
- The output must be using the following structure:


question:
[Sem vložte otázku v slovenčine]


answer:
[Sem vložte odpoveď v slovenčine]


# Steps


1. Read and comprehend the full chapter text.
2. Review and compare the list of previous questions; ensure your question is unique in topic, approach, and detail.
3. Identify a key theme, concept, or area not adequately covered by previous questions.
4. Formulate an open-ended or short-answer question in Slovak targeting that unique aspect.
5. Write a concise, accurate answer that demonstrates deep understanding, again in Slovak.
6. Double-check that your question and answer are both distinct from all previous entries and fully grounded in the provided chapter.


# Output Format


Output only in question and answer pair, like this:


question:
[Sem vložte otázku v slovenčine]


answer:
[Sem vložte odpoveď v slovenčine]


# Examples


Input:

- Provided chapter: [Markdown content about farmakokinetika]
- Previous questions:

  1. Vysvetlite základné štádiá farmakokinetiky a uveďte ich význam pri hodnotení účinnosti liečiv.
  2. Aké faktory ovplyvňujú absorpciu liečiv v tele a prečo sú dôležité v terapeutickej praxi?


Output:

question:
Opíšte význam distribučného objemu (Vd) v farmakokinetike a uveďte, ako môže ovplyvniť dávkovanie liečiv.


answer:
Distribučný objem (Vd) predstavuje pomer množstva liečiva v tele ku koncentrácii liečiva v plazme a je ukazovateľom rozsahu rozptýlenia liečiva v organizme. Veľký Vd znamená, že sa liečivo silne distribuuje do tkanív, zatiaľ čo malý Vd naznačuje, že liečivo zostáva prevažne v plazme. Poznanie Vd je dôležité pre správne stanovenie dávkovania, pretože ovplyvňuje požadovanú dávku na dosiahnutie terapeutickej koncentrácie v krvi.


(Real outputs should address a different central concept or angle than in the previous questions and be several sentences in length.)


# Notes


- Always output only a single question and answer pair in Slovak using the question and answer keys.
- The new question must not duplicate prior questions and should cover new or underrepresented aspects from the provided chapter.
- For long or complex chapters, you may focus on an important subsection not yet covered.
- If you cannot generate a sufficiently different question, select the most distinct topic possible.
- Do not include any introductory or concluding text outside of the required markdown structure.


**Reminder:**  

- Use only Slovak.  
- Base the Q&A strictly on the provided chapter content.  
- Do not repeat or closely echo previous questions.  
- Output only structure as shown.
"""

MAIN_QUESTION_USER_PROMPT = """
- Provided chapter:
{chapter_content}

- Previous questions:
{previous_questions_list}
"""