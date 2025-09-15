"""
HelpDeskBot - simple command-line chatbot using OpenAI.
Requires: Python 3, openai, python-dotenv.
Run with: python main.py (API key in .env).
"""



from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config["API_KEY"]

client = OpenAI(api_key = api_key)



def create_response(paragraph):           #Function for input/output ChatGPT
    response = client.responses.create(
    model="gpt-5",
    input= paragraph)

    print(response.output_text)


print("Welcome! My name is HelpDeskBot and i'm here to answer everything you ask me for!")   #Welcome the User


keep_ask = True

while keep_ask:                                #Creating Cycle to undestand if the user want to ask more questions.
    domanda = input("Cosa ti interessa sapere? ")
    create_response(domanda)
    
    while True:                                 #Cycle to validate the user input 
        more_question = input("Do you want to ask more questions? (Type Y or N) ").strip().upper()
        if more_question == "Y":
            break
        elif more_question == "N":
            print("Thank you for using HelpDeskBot!")
            keep_ask = False
            break
        else:
            print("Invalid input!")
