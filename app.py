import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def build_conversation_dict(msgs: list) -> list[dict]:
    return [
        {"role": "user" if i % 2 == 0 else "assistant", "content": message}
        for i, message in enumerate(msgs)
    ]

def event_stream(conv: list[dict]) -> str:
    response = openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=conv,
        stream=True
    )
    for response_line in response:
        text = response_line.choices[0].delta.get('content', '')
        if len(text):
            yield text

if __name__ == '__main__':
    conversation = build_conversation_dict(msgs=["Bonjour comment ça va ?", "Ça va et toi?"])
    for line in event_stream(conversation):
        print(line)