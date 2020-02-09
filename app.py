from flask import Flask, render_template, request
import json
app = Flask(__name__)

acceptingBuzzes = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main')
def mainsite():
    return render_template("main.html")

@app.route('/login')
def login():
    return render_template("login.html")

#  def create_task():
#      data["tasks"]=[]
#      with open ('tasks.json', 'w') as outfile: 
#          json.dump(data, outfile)

#  def verify_task_complete():
#      with open('tasks.json') as json_file:
#          tasks = json.load(json_file)
#          for task in tasks:
#              if task['initiatior'] == user: 
#                  reward = task["reward"]

@app.route("/authenticate_login", methods=("GET",))
def authenticate_login():
    with open('data/users.json') as json_file:
        users = json.load(json_file)
        for user in users: 
            if request.args["username"] == user: 
                if users[user]["pwdhash"] == request.args["password"]: # hash passwords later!!!
                    return "Success"
                else: 
                    return "Password incorrect"
            else: 
                return "Username not found!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
