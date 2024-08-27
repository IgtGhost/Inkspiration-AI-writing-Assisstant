import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    OPENAI_API_KEY = os.environ.get(
        'OPENAI_API_KEY') or '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'
