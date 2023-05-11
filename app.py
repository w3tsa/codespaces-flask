from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    """Return content from the root level.

    Args: does not take any arguments

    Returns: the route
    """
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    """Return content from the root level.

    Args: does not take any arguments

    Returns: the about route
    """
    return render_template("about.html", title="About")