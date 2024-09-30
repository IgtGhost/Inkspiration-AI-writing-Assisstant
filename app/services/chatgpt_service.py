import openai


openai.api_key = "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"

def generate_chatgpt_response(prompt, temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert creative writer. "
                        "Write detailed, engaging content based on the user's prompt. "
                        "Focus on storytelling, vivid descriptions, and articulate prose to create compelling content."
                    )
                },
                {"role": "user", "content": prompt}
            ],

            temperature=temperature
        )


        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred with ChatGPT: {str(e)}"