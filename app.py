from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

unreadMessages = {
}

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main')
def mainsite():
    return render_template("main.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/get_general_tasks")
def get_general_tasks():
    with open("data/tasks.json", "r") as infile:
        return jsonify(json.load(infile))

#  @app.route("/get_assigned_tasks")
#  def get_general_tasks():
#      with open("data/tasks.json", "r") as infile:
#          tasks = json.load(infile)
#          mytasks = []
#          for task in tasks:
#              if task["assigned"] == request.args["username"]:
#                  mytasks.append(task)
#          return jsonify(mytasks)

@app.route("/createTask")
def createTaskPage():
    return render_template("createTask.html")

@app.route("/createATask")
def createTask():
    with open("data/tasks.json","r") as infile: 
        tasks = json.load(infile)
        largestID = 0
        for task in tasks:
            if task["taskId"] > largestID:
                largestID = task["taskId"]
        new_task = {
            "description": request.args['description'], 
            "initiator":request.args['username'], 
            "estimated_time": request.args["estimated_time"], 
            "reward" : int(request.args['reward']),
            "taskId": largestID+1,
            "assigned": ""
        }
        tasks.append(new_task)
    
    with open ('data/tasks.json', 'w') as outfile: 
        json.dump(tasks, outfile)

    return "success"


@app.route("/acceptTask", methods=("GET",))
def acceptTask():
    taskId = int(request.args["taskId"].replace("generaltask", ""))
    with open('data/tasks.json', "r") as infile:
        tasks = json.load(infile)
        for i in range(len(tasks)):
            task = tasks[i]
            if task["taskId"] == taskId: 
                if task["assigned"] != "": # "" means unasigned
                    return "failure, task assigned already" # note: this never can happen.... probbably wait no lol  general has assigned tasks stoo
                tasks[i]["assigned"] = request.args["username"]
                with open("data/tasks.json", "w") as outfile:
                    json.dump(tasks, outfile)
                return "yay"
    return "nooooo"


    
@app.route("/verify_task_complete", methods=("GET",))
def verify_task_complete():
    taskId = int(request.args["taskId"].replace("mytask", ""))
    with open('data/tasks.json', "r") as infile:
        tasks = json.load(infile)
        for i in range(len(tasks)):
            task = tasks[i]
            if task["taskId"] == taskId: 
                if task["assigned"] =="": # "" means unasigned
                    return "failure, task unassigned"
                reward = task["reward"]
                with open("data/users.json","r") as infile:
                    users = json.load(infile)
                    users[task["assigned"]]["timedimes"]+=reward
                    users[request.args["username"]]["timedimes"]-=reward
                    with open ('data/users.json', 'w') as outfile: 
                        json.dump(users, outfile)

                del tasks[i]
                with open("data/tasks.json", "w") as outfile:
                    json.dump(tasks, outfile)
                return "yay"
    return "nooooo"

@app.route("/create_message", methods=("GET",))
def create_message():
    # message from front end
    with open('data/messages.json', "r") as infile:
        messages = json.load(infile)

        message = {
            "from": request.args["username"], 
            "to": request.args["sendto"], 
            "message": request.args["message"]
        }

        with open("data/users.json", "r") as f:
            toExists = False
            fromExists = False
            users = json.load(f)
            for user in users:
                if user == message["to"]:
                    toExists = True
                if user == message["from"]:
                    fromExists = True
            if not (toExists and fromExists):
                return "failure"

        # TODO: check that sendto is a real person, return False if not real
        messages.append(message)
        try:
            unreadMessages[request.args["username"]].append(message)
        except:
            unreadMessages[request.args["username"]] = [message]
        try:
            unreadMessages[request.args["sendto"]].append(message)
        except:
            unreadMessages[request.args["sendto"]] = [message]

        with open ('data/messages.json', 'w') as outfile: 
            json.dump(messages, outfile)
        return "success"

@app.route("/load_unread_messages", methods=("GET", ))
def load_unread_messages():
    global unreadMessages
    print(unreadMessages)
    try:
        data = unreadMessages[request.args["username"]]
        del unreadMessages[request.args["username"]]
        return jsonify(data)
    except:
        return jsonify([])

@app.route("/load_all_messages", methods=("GET", ))
def load_all_messages():
    user = request.args["username"]
    lst = []
    with open("data/messages.json", "r") as f:
        messages = json.load(f)
        for message in messages:
            print(message)
            if message["from"] == user or message["to"] == user:
                lst.append(message)
    return jsonify(lst)

@app.route("/create_account", methods=("GET",))
def create_account():
    with open('data/users.json', "r") as infile:
        users = json.load(infile)
        for user in users: 
            if request.args["username"] == user: 
                return "name already taken"
        users[request.args["username"]] = {
            "pwdhash": request.args["password"],
            "timedimes": 100,
            "rating": 50,
            "age": 16
            #  "age": request.args["age"]
        }
        with open("data/users.json", "w") as outfile:
            json.dump(users, outfile)
            return "success"
    return "failure"


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
