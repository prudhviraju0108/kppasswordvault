import os
from flask import Flask, render_template,request,redirect,url_for
import yaml
from flask_mysqldb import MySQL
app = Flask(__name__)
db = yaml.load(open("/opt/kpvault/db.yaml"))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route('/add', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        user_name = userdetails['user_name']
        password = userdetails['password']
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("INSERT into details(name,user_name,password) VALUES("'"{0}"'", "'"{1}"'", "'"{2}"'")".format(name,user_name,password))
            mysql.connection.commit()
            cursor.close()
            return "Your entries are successfully added to the list"
        except:
            return "Something went wrong.. Check with system admin to fix the issue"
    return render_template('index.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        deleterequest = request.form
        name = deleterequest['name']
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("DELETE FROM passwordvault.details where name="'"{0}"'"".format(name))
            mysql.connection.commit()
            cursor.close()
            return "Your entry is successfully deleted"
        except:
            return "Something went wrong.. Check with system admin to fix the issue"
    return render_template('delete.html')

@app.route('/dtls')
def dtls():
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute("SELECT * FROM passwordvault.details")
    if resultValue > 0:
        appDetails = cursor.fetchall()
    else: 
        appDetails = "NONE"
    return render_template('details.html',appDetails=appDetails)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'test' or request.form['password'] != 'test':
            error = "Invalid user credentials. Please try again"
        else:
            return redirect(url_for('content'))
    return render_template('login.html', error=error)

@app.route('/content', methods=['GET', 'POST'])
def content():
    return render_template('content.html')

app.run(debug=True,
     host=os.getenv('LISTEN', '0.0.0.0'),
     port=int(os.getenv('PORT', '8080'))
)
