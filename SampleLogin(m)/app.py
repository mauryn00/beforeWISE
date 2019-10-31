import os
from pathlib import Path
from flask import Flask, render_template , redirect , url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import  InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissuppossedtobesecret!'

basedir = Path(__file__).resolve().parents[0]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, r'db\users.db')

Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carmake = db.Column(db.String(80), unique=True, nullable=False,)
    carmodel = db.Column(db.String(80), unique=True, nullable=False,)
    color = db.Column(db.String(80), unique=True, nullable=False,)
    year = db.Column(db.String(4), unique=True, nullable=False,)
    price = db.Column(db.String(20), unique=True, nullable=False,)

class Sbtcrawl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carmake = db.Column(db.String(80), unique=True, nullable=False,)
    #carmodel = db.Column(db.String(80), unique=True, nullable=False,)
    #color = db.Column(db.String(80), unique=True, nullable=False,)
    #year = db.Column(db.String(4), unique=True, nullable=False,)
    price = db.Column(db.String(20), unique=True, nullable=False,)

    # carmodel, carid, year ...

db.create_all()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=80)])
    remember = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
     username = StringField('Username', validators=[InputRequired(),Length(min=4, max=15)])
     password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=80)])
     email = StringField('email', validators = [InputRequired(), Email(message='Invalid email'), Length(max=50)])


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/update", methods=["POST"])
def update():
    try:
        car = Car.query.filter_by(carmake=request.form.get("id")).first()
        car.carmake = request.form.get("make")
        car.carmodel = request.form.get("model")
        car.color = request.form.get("color")
        car.year = request.form.get("year")
        car.price = request.form.get("price")

        db.session.commit()
    except Exception as e:
        print("Failed to Update Car")
        print(e)
    return redirect("/dashboard")

@app.route("/delete", methods=["POST"])
def delete():
    carid = request.form.get("id")
    car = Car.query.filter_by(carid=id).first()
    db.session.delete(car)
    db.session.commit()
    return redirect("/dashboard")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password!</h1>'
           # return '<h1>' + form.username.data + ' ' + form.password.data +
           # '</h1>'
        
    return render_template('login.html', form=form)

@app.route('/signup' , methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username =form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' +
        # form.password.data '</h1>'
        return redirect(url_for('dashboard'))
    
    return render_template('signup.html', form=form)
    

@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    cars = None
    if request.form:
        try:
            car = Sbtcrawl(carmake=request.form.get("carmake"),
                      carmodel=request.form.get("carmodel"),
                      color=request.form.get("color"),
                      year=request.form.get("year"),
                      price=request.form.get("price"))
            db.session.add(car)
            db.session.commit()
        except Exception as e:
            print("Failed to add Car")
            print(e)
    cars = Car.query.all()
    return render_template('dashboard.html', name = current_user.username, cars=cars)

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route("/sales", methods=['GET', 'POST'])
def sales():
    return render_template('sales.html')

@app.route("/inventory", methods=['GET', 'POST'])
def inventory():
    return render_template('inventory.html')

@app.route("/FAQ", methods=['GET', 'POST'])
def FAQ():
    return render_template('FAQ.html')


    

@app.route("/search", methods=['GET', 'POST'])
def search():
    return render_template('search.html')

#@app.route("/refreshdata", methods=['GET', 'POST'])
#def refreshdata():

@app.route("/imports", methods=['GET', 'POST'])
def imports():

    #SBT SITE CRAWL
        option = webdriver.ChromeOptions()
        option.add_argument(" — incognito")
        browser = webdriver.Chrome('C:\\Users\\Maureen Maina\\Desktop\\4.2\\IS PROJECT TOOLS\\chromedriver.exe') 

        browser.get("https://www.sbtjapan.com/used-cars/?t_country=26&sort=5")

# find_elements_by_xpath returns an array of selenium objects.

        ul = browser.find_element_by_class_name("carlist")# work on searching for price as well
        li_items = ul.find_elements_by_tag_name('h2')

    #ul = browser.find_element_by_class_name("totalprices_area")
    #li_items = ul = browser.find_element_by_class_name("car_prices")
        for item in li_items:
            text = item.text
            components = text.split()#splits the string into arrays
            car = Car(id=components[0],
                      carmake=components[1],
                      carmodel=components[2],
                      color=components[3],
                      year=components[4],
                      price=components[5])

            db.session.add(car)
            db.session.commit()
            print(text,'\n')
        
        browser.close();
        return render_template('imports.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))    
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
