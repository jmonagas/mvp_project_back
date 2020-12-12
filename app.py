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
        learner_first_name = request.json.get("learner_first_name")
        learner_middle_name = request.json.get("learner_middle_name")
        learner_last_name = request.json.get("learner_last_name")
        learner_university = request.json.get("learner_university")
        learner_program = request.json.get("learner_program")
        learner_bio = request.json.get("learner_bio")
        learner_email = request.json.get("learner_email")
        learner_phone = request.json.get("learner_phone")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password,
                                   user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO learners (learner_first_name, learner_middle_name, learner_last_name, learner_university, learner_program, learner_bio, learner_email, learner_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
                           learner_first_name, learner_middle_name, learner_last_name, learner_university, learner_program, learner_bio, learner_email, learner_phone])
            rows = cursor.rowcount
            if (rows == 1):
                learner_id = cursor.lastrowid
            conn.commit()
            new_learner = {
                "learner_first_name": learner_first_name,
                "learner_middle_name": learner_middle_name,
                "learner_last_name": learner_last_name,
                "learner_university": learner_university,
                "learner_program": learner_program,
                "learner_bio": learner_bio,
                "learner_email": learner_email,
                "learner_phone": learner_phone,
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
        tutor_first_name = request.json.get("tutor_first_name")
        tutor_middle_name = request.json.get("tutor_middle_name")
        tutor_last_name = request.json.get("tutor_last_name")
        tutor_university = request.json.get("tutor_university")
        tutor_program = request.json.get("tutor_program")
        tutor_bio = request.json.get("tutor_bio")
        tutor_email = request.json.get("tutor_email")
        tutor_phone = request.json.get("tutor_phone")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password,
                                   user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tutors (tutor_first_name, tutor_middle_name, tutor_last_name, tutor_university, tutor_program, tutor_bio, tutor_email, tutor_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
                           tutor_first_name, tutor_middle_name, tutor_last_name, tutor_university, tutor_program, tutor_bio, tutor_email, tutor_phone])
            rows = cursor.rowcount
            if (rows == 1):
                tutor_id = cursor.lastrowid
            conn.commit()
            new_tutor = {
                "tutor_first_name": tutor_first_name,
                "tutor_middle_name": tutor_middle_name,
                "tutor_last_name": tutor_last_name,
                "tutor_university": tutor_university,
                "tutor_program": tutor_program,
                "tutor_bio": tutor_bio,
                "tutor_email": tutor_email,
                "tutor_phone": tutor_phone,
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