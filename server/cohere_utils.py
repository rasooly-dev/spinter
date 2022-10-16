import cohere
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

COHERE_API_KEY = os.getenv('COHERE_API_KEY')
COHERE_API_QUES_TOKENS = int(os.getenv('COHERE_API_QUES_TOKENS'))
COHERE_API_ANS_TOKENS = int(os.getenv('COHERE_API_ANS_TOKENS'))
COHERE_API_TEMPERATURE = float(os.getenv('COHERE_API_TEMPERATURE'))
NUMBER_OF_QUESTIONS = int(os.getenv('NUMBER_OF_QUESTIONS'))
NUMBER_OF_ALTERNATIVES = int(os.getenv('NUMBER_OF_ALTERNATIVES'))

GEN_QUES_PROMPT = """Job Title: {}
Technical Skills: {}
Soft Skills: {}
Job Description: {}
Given the above information, generate one open-ended interview question that an interviewer would ask a candidate with the above technical skills for the job with the given description:
Q1."""

GEN_ANS_PROMPT = """Job Title: {}
Technical Skills: {}
Soft Skills: {}
Job Description: {}
Given the above information, the user was asked the following question:
Q1. {}
Original Response: {}


Create a new improved response to the question using the technical skills:
Improved response:"""


co = cohere.Client(COHERE_API_KEY)  # initalize cohere client


def generate(_prompt, _max_tokens=COHERE_API_QUES_TOKENS):
    response = co.generate(prompt=_prompt,
                           max_tokens=_max_tokens,
                           temperature=COHERE_API_TEMPERATURE,
                           model='xlarge',
                           stop_sequences=["\n"],
                           frequency_penalty=0,
                           presence_penalty=0,
                           p=0.75,
                           k=0)
    return response


def generate_question(criteria):
    tech_str = ""
    soft_str = ""

    for tech in criteria['qualifications']['technical-skills']:
        tech_str += tech + ", "
    for soft in criteria['qualifications']['soft-skills']:
        soft_str += soft + ", "

    prompt = GEN_QUES_PROMPT.format(
        criteria['job-title'], tech_str, soft_str, criteria['job-description'])

    return generate(prompt).generations[0].text.strip()


def generate_questions(criteria, num_questions=NUMBER_OF_QUESTIONS):
    questions = []
    for i in range(num_questions):
        question = generate_question(criteria)
        # questions.append(question.strip()[0:question.strip().rfind('?')+1])
        questions.append(question)

    return questions


def generate_alternative(criteria, response, question):
    tech_str = ""
    soft_str = ""

    for tech in criteria['qualifications']['technical-skills']:
        tech_str += tech + ", "
    for soft in criteria['qualifications']['soft-skills']:
        soft_str += soft + ", "

    prompt = GEN_ANS_PROMPT.format(
        criteria['job-title'], tech_str, soft_str, criteria['job-description'], question, response)
    return generate(prompt, COHERE_API_ANS_TOKENS).generations[0].text.strip()
