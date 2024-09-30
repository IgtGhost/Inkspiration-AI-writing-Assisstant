from flask import render_template, request, redirect, url_for, session, jsonify
from app.services.user_service import register_user, login_user
from app.services.llm_service import generate_content
from app.services.chatgpt_service import generate_chatgpt_response
from app import app

# Secret key for session management
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    # Check if user is logged in
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        full_name = request.form['full_name']
        password = request.form['password']
        email_id = request.form['email_id']

        result = register_user(username, full_name, password, email_id)
        if result['status']:
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error=result['message'])

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = login_user(username, password)
        if result['status']:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error=result['message'])

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/generate', methods=['POST'])
def generate():
    if 'username' not in session:
        return redirect(url_for('login'))

    prompt = request.form.get('prompt', '')
    model_choice = request.form.get('model_choice', 'local')

    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400

    if model_choice == 'local':
        response_text = generate_content(prompt)
    elif model_choice == 'chatgpt':
        response_text = generate_chatgpt_response(prompt)
    else:
        return jsonify({"error": "Invalid model choice."}), 400

    return jsonify({"response": response_text})
