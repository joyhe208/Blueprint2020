from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/main')
def mainsite():
    return render_template("main.html")

@app.route('/login')
def login():
    return render_template("login.html")

def create_task():
    data["tasks"]=[]
    with open ('tasks.json', 'w') as outfile: 
        json.dump(data, outfile)
    
def verify_task_complete():
    with open('tasks.json', "r") as infile:
        tasks = json.load(infile)
        for task in tasks:
            if task['taskID'] == user: # based on id 
                reward = task["reward"]
        with open("users.json","r") as infile:
            users = json.load(infile)
            users[torewardperson]["timedimes"]+=reward
            users[initiator]["timedimes"]-=reward
            with open ('users.json', 'w') as outfile: 
                json.dump(data, outfile)

        del tasks[task]
        with open("tasks.json", "w") as outfile:
            json.dump(tasks)

@app.route("/create_message", methods=("GET",))
def create_message():
    # message from front end
    with open('data/messages.json', "r") as infile:
        messages = json.load(infile)

        # TODO: check that sendto is a real person, return False if not real
        messages.append({"from": request.args["username"], "to": request.args["sendto"], "message": request.args["message"]})
        with open ('data/messages.json', 'w') as outfile: 
            json.dump(messages, outfile)
        return "success"

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
    return "Username not found!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
