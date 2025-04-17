from flask import Flask, render_template, request, flash, redirect, url_for, session
from models.mock_db import store_user, validate_user, mock_db

app = Flask(__name__)
app.secret_key = 'some_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        store_user(name, email, address, username, password, role)
        flash('SUCCESS!!!', 'success')

        return redirect(url_for('login'))

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        role = validate_user(username, password)
        if role:
            session['role'] = role
            session['username'] = username
            flash('Login Successful!!!', 'success')

            if role == 'student':
                return redirect(url_for('student_dashboard'))
            elif role == 'admin':
                return redirect(url_for('admin_dashboard'))
        else:
            flash('INVALID USERNAME OR PASSWORD!!!', 'danger')

    return render_template('login.html')

@app.route('/student_dashboard')
def student_dashboard():
    if 'role' in session and session['role'] == 'student':
        username = session['username']
        user_data = mock_db.get(username)
        return render_template('student_dashboard.html', name=user_data['name'])
    else:
        flash('ACCESS DENIED!!!', 'danger')
        return redirect(url_for('login'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'role' in session and session['role'] == 'admin':
        username = session['username']
        user_data = mock_db.get(username)
        return render_template('admin_dashboard.html', name=user_data['name'])
    else:
        flash('ACCESS DENIED!!!', 'danger')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
