# Standard imports
from flask import render_template, url_for
from flask.helpers import flash
from werkzeug.utils import redirect

# Local imports
from blog import app
from blog.form import RegistrationForm, LoginForm

posts = [
    {
        'author': 'SKriLLCii',
        'title': 'Blog Post 1',
        'content': ' First post content',
        'date_posted': 'April 11, 2022',
    },
    {
        'author': 'SKriLLCii',
        'title': 'Blog Post 2',
        'content': ' Second post content',
        'date_posted': 'April 11, 2022',
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)
