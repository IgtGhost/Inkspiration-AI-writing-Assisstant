from flask import render_template, request, jsonify
from app.services.chatgpt_service import generate_text
from flask import current_app as app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.json.get('text')
    response = generate_text(user_input)
    return jsonify(response)
