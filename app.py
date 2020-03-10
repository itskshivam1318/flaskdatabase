from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_executor import Executor
import detect
import cv2
import time

app = Flask(__name__)

executor = Executor(app)

app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fatigue'

mysql = MySQL(app)

def blink1():
    blink1 = detect.main()
    return blink1


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/exit')
def Exit():
    return render_template('exit.html')


@app.route('/insert', methods=['POST'])
def Insert():
    if request.method == "POST":
        flash("User created Successfully")
        fname = request.form['first_name']
        lname = request.form['last_name']
        email = request.form['email_id']
        gender = request.form['gender']
        age = request.form['age']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(fname, lname, email, gender, age) VALUES (%s, %s , %s, %s, %s)",
                    (fname, lname, email, gender, age))
        mysql.connection.commit()
        return redirect(url_for("Index"))

@app.route('/questions1')
def Questions1():
    #executor.submit(blink1)
    return render_template('questions1.html')

@app.route('/questions2')
def Questions2():
    executor.submit(blink1)
    return render_template('questions2.html')

@app.route('/questions3')
def Questions3():
    executor.submit(blink1)
    return render_template('questions3.html')

@app.route('/questions4')
def Questions4():
    executor.submit(blink1)
    return render_template('questions4.html')


@app.route('/insertques1', methods=['POST'])
def Insertques1():
    if request.method == "POST":
        flash("Answer entered  Successfully")
        que1 = request.form['Question1']
        que2 = request.form['Question2']
        que3 = request.form['Question3']
        que4 = request.form['Question4']
        que5 = request.form['Question5']
        blinks = blink1()
        time.sleep(5)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ques1(`que1`, `que2`, `que3`, `que4`, `que5`,`blinks`) VALUES (%s, %s , %s, %s, %s, %s)",
                    (que1, que2, que3, que4, que5, blinks))
        mysql.connection.commit()
        cv2.destroyAllWindows()
        return redirect(url_for("Questions1"))


@app.route('/insertques2', methods=['POST'])
def Insertques2():
    if request.method == "POST":
        flash("Answer entered  Successfully")
        que1 = request.form['Question1']
        que2 = request.form['Question2']
        que3 = request.form['Question3']
        que4 = request.form['Question4']
        que5 = request.form['Question5']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ques2(`que6`, `que7`, `que8`, `que9`, `que10`) VALUES (%s, %s , %s, %s, %s)",
                    (que1, que2, que3, que4, que5))
        mysql.connection.commit()
        return redirect(url_for("Questions2"))


@app.route('/insertques3', methods=['POST'])
def Insertques3():
    if request.method == "POST":
        flash("Answer entered  Successfully")
        que1 = request.form['Question1']
        que2 = request.form['Question2']
        que3 = request.form['Question3']
        que4 = request.form['Question4']
        que5 = request.form['Question5']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ques3(`que11`, `que12`, `que13`, `que14`, `que15`) VALUES (%s, %s , %s, %s, %s)",
                    (que1, que2, que3, que4, que5))
        mysql.connection.commit()
        return redirect(url_for("Questions3"))


@app.route('/insertques4', methods=['POST'])
def Insertques4():
    if request.method == "POST":
        flash("Answer entered  Successfully")
        que1 = request.form['Question1']
        que2 = request.form['Question2']
        que3 = request.form['Question3']
        que4 = request.form['Question4']
        que5 = request.form['Question5']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ques4(`que16`, `que17`, `que18`, `que19`, `que20`) VALUES (%s, %s , %s, %s, %s)",
                    (que1, que2, que3, que4, que5))
        mysql.connection.commit()
        return redirect(url_for("Questions4"))


if __name__ == "__main__":
    app.run(debug=True)
