import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)
from flask import Flask, request, render_template, url_for, redirect, flash, session
from forms import RegForm, LoginForm, BankForm
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from dominate.tags import img
# ********************* import flask_sqlalchemy *******************************
from flask_sqlalchemy import SQLAlchemy

# ***********import LoginManager class from flask_login module *****************
from flask_login import LoginManager
from flask_login import current_user, login_user, logout_user
from flask_login import login_required


app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=b'this-is-not-very-secure-but-will-work')

# ******************** configure app to link with sqlite database *************, form=form
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ******************** instantiate the SQLAlchemy class with one argument of the Flask app.*************
db = SQLAlchemy(app)

# ********** initialise the LoginManager which binds to app *************, form=form****
login = LoginManager(app)
login.login_view = 'sign_in'

Bootstrap(app)
from models import User, Games

# nav bar implemented here...
logo = img(src='../static/bull2.png', height="50", width="50", style="margin-top:-15px")#here we define our menu items


topbar = Navbar(logo,
                    View('Home', 'home'),
                    View('Logout', 'logout')
                    )


topbar_without_logout = Navbar(logo,
                    View('Home', 'home'),
                    View('Sign in', 'sign_in'),
                    View('Register', 'reg'),
                    )




# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)
nav.register_element('top_without_logout', topbar_without_logout)

@app.route('/', methods=['GET', 'POST'])
def home(): 
    return render_template('index.html')



@app.route('/login/', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:          # ********* this conditional statement deals with a weird situation. Imagine you have a user that is loggedin, and the user navigates to the /login url of your application. Clearly that is a mistake, so we want to prevent that from happeing. We use a redirect to any other route function of our choice....
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username and/or password')
            return redirect(url_for('sign_in'))
            
        login_user(user, remember=True)
        return redirect(url_for('home'))
    return render_template('sign_in.html',form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home'))#

@app.route('/home/')
def home_redirect():
    return render_template('home.html')


@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User(f_name = form.name_first.data, country = form.country_of_residence.data, second_name = form.name_last.data, dob = form.dob.data, address1 = form.adr1.data, address2 = form.adr2.data, postcode = form.postcode.data, email = form.email.data)
        user.set_password(form.password.data)
        user.password = user.password_hash
        db.session.add(user)
        db.session.commit()
        return 'cheddae'
    
    return render_template('register.html', form=form)


nav.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
