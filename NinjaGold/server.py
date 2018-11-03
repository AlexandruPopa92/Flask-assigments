from flask import Flask, render_template, request,redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'alex-secret'
@app.route('/')
def form():
    print("hello")
    
    if not session.get('gold'):
        session['x']=[]

    if not session.get('gold'):
        session['gold']=0
    if not session.get('msg'):
        session['msg']=""
    return render_template('index.html',msg=session['msg'],arr=session['x'])

@app.route('/process_money',methods=['post'])
def count():
    now = datetime.datetime.now()
    if request.form['form'] == 'farm':
        session['rand_farm']=random.randint(10,20)
        session['gold']=session['gold']+session['rand_farm']
        session['msg']= f"<li class='green'>Earned {session['rand_farm']} gold from the farm! ({now.strftime('%Y-%m-%d %H:%M')})</li>"
        session['x'].append(session['msg'])
    elif request.form['form'] == 'cave':
        session['rand_farm']=random.randint(5,10)
        session['gold']=session['gold']+session['rand_farm']
        session['msg']= f"<li class='green'>Earned {session['rand_farm']} gold from the cave! ({now.strftime('%Y-%m-%d %H:%M')})</li>"
        session['x'].append(session['msg'])
    elif request.form['form'] == 'house':
        session['rand_farm']=random.randint(2,5)
        session['gold']=session['gold']+session['rand_farm']
        session['msg']= f"<li class='green'>Earned {session['rand_farm']} gold from the house! ({now.strftime('%Y-%m-%d %H:%M')})</li>"
        session['x'].append(session['msg'])
    else:
        session['rand_farm']=random.randint(-50,50)
        session['gold']=session['gold']+session['rand_farm']
        session['msg']= f"<li class='red'>Entered casino and lost {session['rand_farm']}gold...Ouch! ({now.strftime('%Y-%m-%d %H:%M')})</li>"
        session['x'].append(session['msg'])

    return redirect("/")

@app.route('/delete',methods=['post'])
def delete():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)