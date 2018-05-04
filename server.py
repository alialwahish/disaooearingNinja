from flask import Flask,render_template,redirect,request
app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template("index.html")
@app.route('/ninja')
def process():
    return render_template("ninja.html")
@app.route('/process',methods=["POST"])
def ninColor():
    color=request.form["color"]
    print color
    return render_template("oneNinja.html",color=color)
app.run(debug=True)