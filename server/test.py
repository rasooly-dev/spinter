from cohere_utils import *

criteria = {'job-title': 'Software Developer',
            'qualifications': {'technical-skills': ['Python', 'CSS', 'HTML', 'Javascript', 'frontend', 'backend'],
                               'soft-skills': ['Patience', 'determination', 'time management', 'responsibility']},
            'job-description': 'In need of a software developer who has good problem solving skills and can manage big projects while working as a team.'}

questions = generate_questions(criteria)
print(questions[0])
answer = input('Type a response: ')
alternative_answers = []
for i in range(3):
    alternative_answers.append(
        generate_alternative(criteria, answer, questions[0]))
for alt in alternative_answers:
    print(alt + '\n')
