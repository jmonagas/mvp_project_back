import dbcreds
import mariadb
from flask import Flask, request, Response
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Route to '/api/learners' --------------------


@app.route('/api/learners', methods=["POST"])
def learnersAll():
    if request.method == "POST":
        conn = None
        cursor = None
        first_name = request.json.get("first_name")
        middle_name = request.json.get("middle_name")
        last_name = request.json.get("last_name")
        university = request.json.get("university")
        program = request.json.get("program")
        bio = request.json.get("bio")
        email = request.json.get("email")
        phone = request.json.get("phone")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password,
                                   user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO learners (first_name, middle_name, last_name, university, program, bio, email, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
                           first_name, middle_name, last_name, university, program, bio, email, phone])
            rows = cursor.rowcount
            if (rows == 1):
                learner_id = cursor.lastrowid
                print(learner_id)
            conn.commit()
            new_learner = {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "university": university,
                "program": program,
                "bio": bio,
                "email": email,
                "phone": phone,
            }
            sendLearner = json.dumps(new_learner)
        except Exception as error:
            print("New Learner Registration Method Failed")
            print(error)
        finally:
            if (cursor != None):
                cursor.close()
            if (conn != None):
                conn.rollback()
                conn.close()
            if (rows == 1):
                return Response("Success! New Learner Was Added", mimetype="text/html", status=201)
            else:
                return Response("Error! New Learner Was Not Added", mimetype="text/html", status=500)


# Route to '/api/tutors' --------------------


@app.route('/api/tutors', methods=["POST"])
def tutorsAll():
    if request.method == "POST":
        conn = None
        cursor = None
        first_name = request.json.get("first_name")
        middle_name = request.json.get("middle_name")
        last_name = request.json.get("last_name")
        university = request.json.get("university")
        program = request.json.get("program")
        bio = request.json.get("bio")
        email = request.json.get("email")
        phone = request.json.get("phone")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password,
                                   user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tutors (first_name, middle_name, last_name, university, program, bio, email, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
                           first_name, middle_name, last_name, university, program, bio, email, phone])
            rows = cursor.rowcount
            if (rows == 1):
                tutor_id = cursor.lastrowid
                print(tutor_id)
            conn.commit()
            new_tutor = {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "university": university,
                "program": program,
                "bio": bio,
                "email": email,
                "phone": phone,
            }
            sendTutor = json.dumps(new_tutor)
        except Exception as error:
            print("New Tutor Registration Method Failed")
            print(error)
        finally:
            if (cursor != None):
                cursor.close()
            if (conn != None):
                conn.rollback()
                conn.close()
            if (rows == 1):
                return Response("Success! New Tutor Was Added", mimetype="text/html", status=201)
            else:
                return Response("Error! New Tutor Was Not Added", mimetype="text/html", status=500)