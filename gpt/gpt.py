import openai
import os

def chat_completion(prompt: list, query: str) -> str:
    """
    This function is used to generate a response to a query using the OpenAI API for gpt 3.5 TURBO.
    
    Parameters
    ----------
    prompt : list
        A preset prompt that will be used to generate the response.
        query : str
        The query that will be used to generate the response.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt.append({"role": "user", "content": query})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompt)
    return response.choices[0].message.content
    