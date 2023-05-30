from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Set a secret key for session management

# Mock database for storing user information (replace with a real database in production)
users = []

@app.route('/')
def home():
    return "Welcome to BingeBuddies!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)  # Hash the password before storing

        # Check if the username is already taken
        if any(user['username'] == username for user in users):
            return "Username already exists. Please choose a different username."

        # Store the user information in the database
        users.append({'username': username, 'password': hashed_password})

        # Redirect the user to the login page
        return redirect('/login')
    else:
        return render_template('register.html')  # Display the registration form

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists in the database
        user = next((user for user in users if user['username'] == username), None)
        if not user:
            return "Username not found. Please check your username or register a new account."

        # Check if the password matches
        if not check_password_hash(user['password'], password):
            return "Incorrect password. Please try again."

        # Store the username in the session to maintain user login
        session['username'] = username

        # Redirect the user to the main dashboard or profile page
        return redirect('/dashboard')
    else:
        return render_template('login.html')  # Display the login form

@app.route('/logout')
def logout():
    # Clear the session and redirect the user to the login page
    session.clear()
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'username' in session:
        # Retrieve the user's information from the database and display the dashboard
        return "Welcome to your BingeBuddies dashboard, {}".format(session['username'])
    else:
        return "You are not logged in. Please log in or register an account."

if __name__ == '__main__':
    app.run(debug=True)
