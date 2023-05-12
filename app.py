# pylint: disable=missing-function-docstring


"""
Module docstring goes here.
"""
from datetime import datetime
from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

db = SQLAlchemy()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hcnv6ARXyr2fqQazuYLFQ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# pylint: disable=missing-class-docstring
db.init_app(app)

# pylint: disable=too-few-public-methods
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}'"

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

user_1 = User(username='some', email='t3@email.com', password='pass')
user_2 = User(username='some other', email='s3@email.com', password='pass')

with app.app_context():
    db.create_all()
    db.session.add(user_2)
    db.session.commit()


@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("users.html", users=users, title='Users')

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
