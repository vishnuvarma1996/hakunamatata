from flask import Flask
from flask import render_template
from flask import request
import sqlite3


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/chart")
def chart():
    return render_template('chart.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/updateuser", methods = ['POST', 'GET'])
def updateuser():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']

        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("UPDATE USER SET PASSWORD=? WHERE USERNAME=?",(pwd, username,))
            conn.commit()
    return render_template('homepage.html')

@app.route("/deleteuser", methods = ['POST', 'GET'])
def deleteuser():
    if request.method == 'POST':
        username = request.form['username']
        print("The user name is " + username)
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM USER WHERE USERNAME=?",(username,))
            conn.commit()
    return render_template('index.html')

@app.route("/validateuser", methods = ['POST', 'GET'])
def validateuser():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            user = cur.execute("SELECT * FROM USER where username = ?",(username,)).fetchone()

            errors = []
            if user == None:
                errors.append("User doesnt exist please signup if you are a first time user")
                return render_template('index.html', errors = errors )
            
            if(user[1] == pwd):
                return render_template('homepage.html')
            
            else:
                errors.append("Incorrect username or password please try again")
                return render_template('index.html', errors = errors )
                

@app.route("/signupuser", methods = ['POST', 'GET'])
def signupuser():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        print("fh user")
        with sqlite3.connect('database.db') as conn:
            
            cur = conn.cursor()
            cur.execute("INSERT INTO USER (username, password) VALUES (?, ?)", (username, pwd))
            print("insert executed successfully!")
            conn.commit()
            message = "User Signed up Successfully"
            return render_template('homepage.html')


if __name__ == '__main__':
    app.run()