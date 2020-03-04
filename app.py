from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fatigue'

mysql = MySQL(app)


@app.route('/')
def Index():
    return render_template('index.html')


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


@app.route('/questions')
def Questions():
    return render_template('questions.html')
'''
@app.route('/insertques', methods=['POST'])
def Insertques():
    if request.method == "POST":
        flash("Answer entered  Successfully")

        que1 = request.form['que1']
        que2 = request.form['que2']
        que3 = request.form['que3']
        que4 = request.form['que4']
        que5 = request.form['que5']
        que6 = request.form['que6']
        que7 = request.form['que7']
        que8 = request.form['que8']
        que9 = request.form['que9']
        que10 = request.form['que10']
        que11 = request.form['que11']
        que12 = request.form['que12']
        que13 = request.form['que13']
        que14 = request.form['que14']
        que15 = request.form['que15']
        que16 = request.form['que16']
        que17 = request.form['que17']
        que18 = request.form['que18']
        que19 = request.form['que19']
        que20 = request.form['que20']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ques(fname, lname, email, gender, age) VALUES (%s, %s , %s, %s, %s)",
                    (fname, lname, email, gender, age))
        mysql.connection.commit()
        return redirect(url_for("Index"))
'''

if __name__ == "__main__":
    app.run(debug=True)
