import openai
from flask import current_app
from openai.error import RateLimitError


def generate_text(prompt):
    openai.api_key = current_app.config['OPENAI_API_KEY']
    print(f"Using API key: {openai.api_key}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except RateLimitError as e:
        # Handle rate limit error, perhaps log it and inform the user
        return "API quota exceeded. Please try again later."
