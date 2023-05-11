# pylint: disable=missing-function-docstring

"""
Module docstring goes here.
"""

from flask import Flask, render_template, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hcnv6ARXyr2fqQazuYLFQ'

posts = [
    {
        'author': 'Tanveer Sayem',
        'title': 'Blog post',
        'content': 'First post content',
        'date_posted': 'May 11, 2023'
    },
    {
        'author': 'Rahim Shah',
        'title': 'Blog post 2',
        'content': 'Seccond post content',
        'date_posted': 'May 11, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect('home')
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect('home')
        else:
            flash('Log in Unsuccessful. Please check username and password', 'danger') 
    return render_template('login.html', title='Login', form=form)
