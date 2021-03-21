from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def run ():
    return render_template("IOT-7/index.html")
@app.route('/btna')
def btna():
    return "button1"

@app.route ('/btnb')
def btnb ():
    return "button2"

if __name__ == '__main__':
    app.run()
    