from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())  # looking for .env file
openai_key = os.getenv("OPENAI_API_KEY")

messages = []
openai_client = OpenAI(api_key=openai_key)

def call_api(model_chat, messages, temperature): 
        try:
            response = openai_client.chat.completions.create(
            model=model_chat,
            messages=messages,
            temperature=temperature,
        )
        except Exception as e:
            print(e)
        else:
            add_message("assistant", response.choices[0].message.content)
            return response.choices[0].message.content

def add_message(role, content):
        json_message = {
            "role": role, 
            "content": content
        }
        messages.append(json_message)

def ask_question(question):
    add_message("system", "You are an expert in python, data science, artificial intelligence and machine learning")
    add_message("user", question)
    print("-" * 67)
    print("Your question is: ", question)
    print("-" * 67)
    print(call_api("gpt-3.5-turbo", messages, 0.5))

def main():
    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Exiting...")
            break
        ask_question(question)

if __name__ == "__main__":
    main()