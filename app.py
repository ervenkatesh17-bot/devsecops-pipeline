import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Secure Pipeline!"

@app.route('/login', methods=['POST'])
def login():
    # VULNERABILITY: Hardcoded password (Security Scanner isse pakdega)
    secret_password = "admin_password_123" 
    
    username = request.form.get('username')
    if username == "admin":
        return "Access Granted"
    return "Access Denied"

if __name__ == '__main__':
    app.run(debug=True)
