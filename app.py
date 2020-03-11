from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_executor import Executor
from multiprocessing import Process
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from detect import eye_aspect_ratio
import imutils
import dlib
import cv2
import time

class processClass:
    def __init__(self):
        p = Process(target=self.run, args=())
        p.daemon = True  # Daemonize it
        p.start()

    def eye_aspect_ratio(eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def run(self):
        EYE_AR_THRESH = 0.27
        EYE_AR_CONSEC_FRAMES = 2
        shape_predictor = "shape_predictor_68_face_landmarks.dat"
        COUNTER = 0
        TOTAL = 0
        print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(shape_predictor)
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        print("[INFO] starting video stream thread...")
        print("[INFO] print q to quit...")
        vs = VideoStream(src=0).start()
        while True:
            frame = vs.read()
            frame = imutils.resize(frame, width=450)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rects = detector(gray, 0)
            for rect in rects:
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
                ear = (leftEAR + rightEAR) / 2.0
                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
                if ear < EYE_AR_THRESH:
                    COUNTER += 1
                else:
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        TOTAL += 1
                    COUNTER = 0
                #cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                #cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            file = open('out.txt', 'w')
            file.write(str(TOTAL))
            file.close()
            #cv2.imshow("Frame", frame)


app = Flask(__name__)

executor = Executor(app)

app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fatigue'

mysql = MySQL(app)



@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/exit')
def Exit():
    cv2.destroyAllWindows()
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
    begin = processClass()
    return render_template('questions1.html')

@app.route('/questions2')
def Questions2():
    return render_template('questions2.html')

@app.route('/questions3')
def Questions3():
    return render_template('questions3.html')

@app.route('/questions4')
def Questions4():
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
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ques1(`que1`, `que2`, `que3`, `que4`, `que5`) VALUES (%s, %s , %s, %s, %s)",
                    (que1, que2, que3, que4, que5))
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
        fileread = open('out.txt', 'r')
        dataread = fileread.readlines()
        print(dataread)
        data = str(dataread[0])
        print(data)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ques4(`que16`, `que17`, `que18`, `que19`, `que20`,`blink`) VALUES (%s, %s , %s, %s, %s, %s)",
                    (que1, que2, que3, que4, que5, data))
        mysql.connection.commit()
        return redirect(url_for("Questions4"))


if __name__ == "__main__":
    app.run(debug=True)
