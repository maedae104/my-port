from flask import (Flask, redirect, render_template, request,
                    flash, session)
from jinja2 import StrictUndefined

app = Flask(__name__   )
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """Show the application's homepage."""

    return render_template('homepage.html')


@app.route('/resume')
def show_resume():
    """Show resume."""

    return render_template('resume.html')

@app.route('/projects')
def show_projects():
    """Show projects."""

    return render_template('projects.html')

@app.route('/about')
def show_about():
    """Show about."""

    return render_template('about.html')   


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", debug=True)