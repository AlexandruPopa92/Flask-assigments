from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    print("Welcome!!!")
    return "Welcome!!!"

@app.route('/play')
def play_1():
    print("Welcome lvl1!!!")
    return render_template('index.html', repeat=3,times=0)

@app.route('/play/<x>')
def play_2(x):
    print("Welcome lvl2!!!")
    return render_template('index.html',times=int(x),repeat=0)

@app.route('/play/<x>/<color>')
def play_3(x,color):
    print("Welcome lvl2!!!")
    return render_template('index.html',times=int(x),repeat=0,paint=color)


if __name__=="__main__":
    app.run(debug=True) 