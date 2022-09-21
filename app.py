from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def index():

    return render_template('hotjob.html')


@app.route('/job')
def job():

    return render_template('hotjob.html')


@app.route('/form')
def form():

    return render_template('form.html')


@app.route('/Form job')
def Formjob():

    return render_template('Form job.html')

if __name__=='__main__':
    app.run(debug=True)


