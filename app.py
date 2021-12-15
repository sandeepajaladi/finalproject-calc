# Route for handling the login page logic
import os
from threading import Thread
from flask.sessions import NullSession
import pandas as pd
from os import error, name
from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from werkzeug.utils import secure_filename
from flask import g
import logging
from prettytable import PrettyTable

from classes.Claculation import Calculation
#from main import second


app = Flask(__name__)
app.config['UPLOAD_PATH'] = r'/Users/sujayjaladi/Downloads/sandeepaflask'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
#logging.basicConfig(filename='calculations.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt="%d/%m/%Y %H:%M:%S")
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#app.config["SECRET_KEY"] = 'shhhhhhhhhhh!!'

#Session(app)

#app.register_blueprint(second,url_prefix='/admin')

@app.route('/index',methods=['GET','POST'])
def home():
    return render_template('index.html',error=error)

@app.route('/Python Glossary')
def pythontuttorial():
   return render_template('Python Glossary.html',error=error)

@app.route('/ecommerce')
def ecommerce():
   return render_template('ecommerce.html',error=error)	

@app.route('/pylint')
def pylint():
   return render_template('Pylint.html',error=error)	

@app.route('/oopsconcepts')
def oopsconcepts():
   return render_template('Oops concepts.html',error=error)

@app.route('/socialnetworking')
def socialnetworking():
   return render_template('socialnetworking.html',error=error)


@app.route('/calculator',methods=['GET', 'POST'])
def calculator():
   if request.method == 'POST':
      n1 = request.form['fnum1']
      n2 = request.form['fnum2']
      op = request.form['operat']
      c1 = Calculation(n1,n2,op)
      c1.operation()
      return redirect(url_for('calculator'))
   return render_template('calculator.html',error=error)

@app.route('/serachengine')
def searchengine():
   return render_template('searchengine.html',error=error)

@app.route('/AAATesting')
def AAATesting():
   return render_template('AAA Testing.html',error=error) 

@app.route('/SOLID principles')
def SOLIDprinciples():
   return render_template('SOLID principles.html',error=error)

@app.route('/result')
def result():
   filename = "History.csv"
   data = pd.read_csv(os.path.join(app.config['UPLOAD_PATH'],filename),dtype=object);

   htmlfile = open(r'/Users/sujayjaladi/Downloads/sandeepaflask/result.html', 'w')
   result = data.to_html()
   htmlfile.write(result)
   htmlfile.close()

   return render_template('result.html', tables=[result], error=error, titles=['na', 'Calculator Result Data'])


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
