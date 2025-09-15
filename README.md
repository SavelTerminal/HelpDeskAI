# HelpDeskAI

A simple command-line chatbot powered by OpenAI.
It asks the user for input, sends it to the API, and prints the response.

## Setup

Clone this repository

Install dependencies:
pip install python-dotenv openai

Create a file named ".env" in the project root with your API key:
API_KEY=your_openai_api_key_here

### Run
From the project folder, run:
python main.py

#Notes

".env" is not included in the repo (see the provided ".env.example").

The bot will keep asking questions until you type N.
