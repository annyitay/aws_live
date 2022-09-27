from flask import  Flask, render_template, request, jsonify, redirect, url_for
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('EmpPanel.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.intellipaat.com')


@app.route("/searchemp", methods=['GET', 'POST'])
def search():
    return render_template('SearchEmp.html')

@app.route("/addempdata", methods=['GET', 'POST'])
def addEmpdata():
    return render_template('AddEmp.html')

@app.route("/editemp", methods=['GET', 'POST'])
def editEmp():
    return render_template('EditEmp.html')

@app.route("/cancelButton", methods=['GET', 'POST'])
def back():
    return render_template('EmpPanel.html')

@app.route("/deleteemp", methods=['GET', 'POST'])
def deleteEmp():
    return render_template('DeleteEmp.html')

@app.route("/removeEmp",methods=['POST'])
def RemoveEmp():
    emp_id = request.form.get("emp_ids")
    remove_sql = "Delete from employee where emp_id = %s"
    cursor = db_conn.cursor()
    cursor.execute(remove_sql, (emp_id))
    db_conn.commit()

    return render_template("EmpPanel.html")

@app.route("/editEmp",methods=['POST'])
def EditEmp():
    f_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    pri_skill = request.form.get("pri_skill")
    location = request.form.get("location")
    email = request.form.get("email")
    salary = request.form.get("salary")
    emp_id = request.form.get("emp_ids")

    update_sql = "Update employee Set first_name = %s, last_name = %s, pri_skill = %s, location = %s,email = %s,salary = %s where emp_id = %s"
    cursor = db_conn.cursor()

    cursor.execute(update_sql, (f_name, last_name, pri_skill, location, email ,salary,emp_id))
    db_conn.commit()

    return render_template('EmpPanel.html')

@app.route("/retrieveEditEmp",methods=['POST','GET'])
def RetrieveEmp():
    searchbox = request.form.get("emp_id")
    cursor = db_conn.cursor()

    query = "SELECT first_name FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query)
    first_name = cursor.fetchone()
    first_name = ''.join(first_name)

    query2 = "SELECT last_name FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query2)
    last_name = cursor.fetchone()
    last_name = ''.join(last_name)

    query3 = "SELECT pri_skill FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query3)
    pri_skill = cursor.fetchone()
    pri_skill = ''.join(pri_skill)


    query4 = "SELECT location FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query4)
    location = cursor.fetchone()
    location = ''.join(location)

    query5 = "SELECT email FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query5)
    email = cursor.fetchone()
    email = ''.join(email)


    query6 = "SELECT salary FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query6)
    salary = cursor.fetchone()
    salary = ''.join(salary)


    return render_template('EditEmp.html',first_name = first_name, last_name = last_name,pri_skill = pri_skill
    ,location = location, email = email,salary = salary,emp_id = searchbox)

@app.route("/retrieveDeleteEmp",methods=['POST','GET'])
def RetrieveEmp():
    searchbox = request.form.get("emp_id")
    cursor = db_conn.cursor()

    query = "SELECT first_name FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query)
    first_name = cursor.fetchone()
    first_name = ''.join(first_name)

    query2 = "SELECT last_name FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query2)
    last_name = cursor.fetchone()
    last_name = ''.join(last_name)

    query3 = "SELECT pri_skill FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query3)
    pri_skill = cursor.fetchone()
    pri_skill = ''.join(pri_skill)


    query4 = "SELECT location FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query4)
    location = cursor.fetchone()
    location = ''.join(location)

    query5 = "SELECT email FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query5)
    email = cursor.fetchone()
    email = ''.join(email)


    query6 = "SELECT salary FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query6)
    salary = cursor.fetchone()
    salary = ''.join(salary)


    return render_template('DeleteEmp.html',first_name = first_name, last_name = last_name,pri_skill = pri_skill
    ,location = location, email = email,salary = salary,emp_id = searchbox)

@app.route("/retrieveSearchEmp",methods=['POST','GET'])
def RetrieveEmp():
    searchbox = request.form.get("emp_id")
    cursor = db_conn.cursor()

    query = "SELECT first_name FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query)
    first_name = cursor.fetchone()
    first_name = ''.join(first_name)

    query2 = "SELECT last_name FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query2)
    last_name = cursor.fetchone()
    last_name = ''.join(last_name)

    query3 = "SELECT pri_skill FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query3)
    pri_skill = cursor.fetchone()
    pri_skill = ''.join(pri_skill)


    query4 = "SELECT location FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query4)
    location = cursor.fetchone()
    location = ''.join(location)

    query5 = "SELECT email FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query5)
    email = cursor.fetchone()
    email = ''.join(email)


    query6 = "SELECT salary FROM employee WHERE emp_id = '{}'".format(searchbox)
    cursor.execute(query6)
    salary = cursor.fetchone()
    salary = ''.join(salary)


    return render_template('SearchEmp.html',first_name = first_name, last_name = last_name,pri_skill = pri_skill
    ,location = location, email = email,salary = salary,emp_id = searchbox)

@app.route("/addEmp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    email = request.form['email']
    salary = request.form['salary']
    password = request.form['pass']
    location = request.form['location']
    emp_image_file = request.files['emp_image_file']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"

    try:

        cursor.execute(insert_sql, (emp_id, first_name, last_name, pri_skill, location,email,salary,password))
        db_conn.commit()
        emp_name = "" + first_name + " " + last_name
        # Uplaod image file in S3 #
        emp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file"
        s3 = boto3.resource('s3')

        try:
            print("Data inserted in MySQL RDS... uploading image to S3...")
            s3.Bucket(custombucket).put_object(Key=emp_image_file_name_in_s3, Body=emp_image_file)
            bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
            s3_location = (bucket_location['LocationConstraint'])

            if s3_location is None:
                s3_location = ''
            else:
                s3_location = '-' + s3_location

            object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                s3_location,
                custombucket,
                emp_image_file_name_in_s3)

        except Exception as e:
            return str(e)

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=emp_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
