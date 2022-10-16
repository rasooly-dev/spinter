import cohere
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
COHERE_API_TOKENS = os.getenv('COHERE_API_TOKENS')
COHERE_API_TEMPERATURE = os.getenv('COHERE_API_TEMPERATURE')
NUMBER_OF_QUESTIONS = os.getenv('NUMBER_OF_QUESTIONS')


co = cohere.Client(COHERE_API_KEY)  # initalize cohere client


def generate(_prompt):
    response = co.generate(prompt=_prompt,
                           max_tokens=COHERE_API_TOKENS,
                           temperature=COHERE_API_TEMPERATURE)
    return response


def generate_questions_and_answers(criteria):
    base_prompt = f"Job Title: {criteria['job-title']}\n"\
        f"Soft Skills: {criteria['qualifications']['soft-skills']}\n"\
        f"Technical Skills: {criteria['qualifications']['technical-skills']}\n"\
        f"Job Description: {criteria['job-description']}\n"

    if criteria['interview-questions']:
        questions = criteria['interview-questions']
    else:
        questions_prompt = base_prompt + f"Given the information above, generate {NUMBER_OF_QUESTIONS} "\
            "interview questions separated by commas for this job position:\n"
        # need to parse this output to match the one from the if statement
        questions = generate(questions_prompt).generations[0].text.split(",")
        questions = [question.strip() for question in questions]

    answers = []
    for question in questions:
        answer_prompt = base_prompt + \
            f"Given the information above, answer the following question: {question}\n Answer: "
        answers.append(generate(answer_prompt).generations[0].text.strip())

    question_answer_pairs = []
    for i in range(len(questions)):
        question_answer_pairs.append(
            {'question': questions[i], 'preferred-answer': answers[i]})

    data = {'data': question_answer_pairs}
    return json.dumps(data)


def generate_improved_answer(criteria, response, filler_words, common_words):
    pass
