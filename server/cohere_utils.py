import cohere
co = cohere.Client('{apiKey}')

def generate_questions(_prompt, _tokens, _temperature):
    response = co.generate(prompt=_prompt, max_tokens=_tokens, temperature=_temperature)
    return response

