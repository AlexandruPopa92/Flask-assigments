from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html",row_start=int(8), row=8)

@app.route('/<x>')
def print_x(x):
    return render_template("index.html", row=int(x),row_start=int(8))





if __name__=="__main__":
    app.run(debug=True)
