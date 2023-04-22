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
    new_prompt = []
    new_prompt.append(prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    new_prompt.insert(0, {"role": "system", "content": "You are a chatbot assistant that listens to your user's instructions carefully and follows them."})
    new_prompt.append({"role": "user", "content": query})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=new_prompt)
    return response.choices[0].message.content
    
