from flask import Flask, redirect, url_for, render_template, request, session, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdashdkashdasp2131231231sadhagsdgad123oi1hoaisipd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
db = SQLAlchemy(app)






class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(30), unique = True , nullable=False)
    password = db.Column(db.String(80), nullable=False)





@app.route('/')
def main():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")
 
@app.route('/movies')
def moives():
    return render_template("movies.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        passw= request.form['password']
        user1 = User(username = user , password = generate_password_hash(passw))
        db.session.add(user1)
        db.session.commit()
        session['username']= user
        return redirect('/home')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/home')

if __name__=="__main__":
    app.run(debug=True)

