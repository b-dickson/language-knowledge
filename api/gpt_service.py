import openai
from config.secret import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

MODEL = "gpt-4"
def generate_sparql_query(question, feedback=None):
    initial_message = {
        "role": "system",
        "content": "Translate the following question into a SPARQL query for DBPEDIA. Include the proper prefixes."
    }
    user_message = {"role": "user", "content": question}

    messages = [initial_message, user_message]

    response = openai.ChatCompletion.create(model=MODEL, messages=messages)
    sparql_query = response['choices'][0]['message']['content'].strip()

    initial_message = {
        "role": "system",
        "content": "Is this an accurate SPARQL query for the question? If not, please respond only with a rewritten query to better fit the question. If it is, please respond only with the original query."
    }
    user_message = {"role": "user", "content": f"query: {sparql_query}, question: {question}"}

    messages = [initial_message, user_message]

    response = openai.ChatCompletion.create(model=MODEL, messages=messages)
    sparql_query = response['choices'][0]['message']['content'].strip()

    return sparql_query


def interpret_sparql_query(question, response):
    messages = [
        {"role": "system", "content": f"Use the information provided from the follwing SPARQL query response to provide an answer the original question."},

        {"role": "user", "content": f'''Original question: {question}, SPARQL query response: {response}'''}
    ]

    respond = openai.ChatCompletion.create(model=MODEL, messages=messages)
    answer = respond['choices'][0]['message']['content'].strip()
    return answer

