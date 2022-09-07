from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def index():

    return render_template('hotjob.html')


@app.route('/job')
def job():

    return render_template('job.html')

if __name__=='__main__':
    app.run(debug=True)


