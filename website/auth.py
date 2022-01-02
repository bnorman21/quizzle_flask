from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

#post request means you are making some type of change to the state of the system
#get request is retrieveing information

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")



@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than one character', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be 7 characters or more', category='error')
        else:
             flash('Account created!', category='success')
    return render_template("sign_up.html")

