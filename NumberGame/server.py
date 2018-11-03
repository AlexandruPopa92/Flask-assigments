from flask import Flask, render_template, request,redirect, session
import random
app = Flask(__name__)
app.secret_key = 'alex-secret'

@app.route('/')
def form():
    app.logger.info("hello")
    if 'x' in session:
        app.logger.info('key exist!')
    else:
        session['insert_number'] = 0
        if not session.get('rand'):
            session['rand']=random.randint(1,100)
        if not session.get('status'):
            session['status'] = "blah"

    app.logger.info("Status so far: %s", session['status'])
    return render_template('index.html', num=session['status'])

@app.route('/form',methods=['post'])
def count():
    session['insert_number']=request.form['insert']
    app.logger.info(">>>>>> Getting here")
    if int(session['insert_number'])==int(session['rand']):
        app.logger.info(">>>>>> EQUAL")
        session['status'] = "equal"
    elif int(session['insert_number'])>int(session['rand']):
        app.logger.info(">>>>>> HIGH")
        session['status'] = "high"
    else:
        app.logger.info(">>>>>> LOW")
        session['status'] = "low"

    return redirect("/")

@app.route('/delete',methods=['post'])
def delete():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)