from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('search.search'))  # or dashboard
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    print("Serving login page...")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            return redirect(url_for('search.search'))
        else:
            return "Invalid credentials. Please try again."

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@auth_bp.before_request
def clear_session_on_restart():
    if request.endpoint == 'login' and 'username' in session:
        # Optionally remove this in production
        session.clear()