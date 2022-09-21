import datetime

from sqlalchemy import *
import pandas as pd
from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def index():

    return render_template('hotjob.html')


@app.route('/job')
def job():

    return render_template('job.html')

@app.route('/Form job')
def Formjob():

    return render_template('Form job.html')

@app.route('/add_record', methods=['POST','GET'])

def add_record():
    
    if request.method=='POST':
        
        title = request.form['title']
        description = request.form['description']
        responsibility= request.form['responsibility']
        salary = request.form['salary']
        deadline = request.form['deadline']
        
        engine=create_engine('postgresql://gnmhchujqyhrzj:fd09407ece6935d2ba46fcda5e6ee46f6bf31d283a3ae4b2ff4cd3a0c6520e08@ec2-52-200-5-135.compute-1.amazonaws.com:5432/dd06j8l9gh4f42')

        dbConnection    = engine.connect();
        
        df=pd.read_sql("select * from jobs",dbConnection)  #read table
        df=df.set_index('Job_id')
        
        dateposted = datetime.datetime.now().date()
        
        df.loc[len(df)] = [title,description,responsibility,dateposted,salary,deadline]
        df.to_sql('jobs', dbConnection,if_exists='replace')  #creste table
        
        
        return render_template('Form job.html', msg='Sucessfully uploaded record')


              
if __name__=='__main__':
    app.run(debug=True)

