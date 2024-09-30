from pymongo import MongoClient
from flask_bcrypt import Bcrypt

# MongoDB connection
client = MongoClient('mongodb+srv://chauhandhruv903:6969@cluster0.bpu9v4a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['flask_chatbot_app']  # Database name
users_collection = db['users']  # Collection name

# Bcrypt for password hashing
bcrypt = Bcrypt()


def register_user(username, full_name, password, email_id):
    # Check if username or email already exists
    if users_collection.find_one({"username": username}) or users_collection.find_one({"email_id": email_id}):
        return {"status": False, "message": "Username or email already exists."}

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Insert user data into the database
    user_data = {
        "username": username,
        "full_name": full_name,
        "password": hashed_password,
        "email_id": email_id
    }
    users_collection.insert_one(user_data)
    return {"status": True, "message": "User registered successfully."}


def login_user(username, password):
    # Find user in the database
    user = users_collection.find_one({"username": username})
    if user and bcrypt.check_password_hash(user['password'], password):
        return {"status": True, "message": "Login successful."}
    return {"status": False, "message": "Invalid username or password."}
