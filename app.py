from flask import Flask, render_template, request
import json
app = Flask(__name__)

acceptingBuzzes = True

@app.route('/')
def index():
    return render_template("index.html")

# temporary
@app.route('/main')
def mainthing():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
