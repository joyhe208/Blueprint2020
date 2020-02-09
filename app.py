from flask import Flask, render_template, request
import json
app = Flask(__name__)

acceptingBuzzes = True

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


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
        
        
        

def create_message():
    # message from front end
    with open('messages.json', "r") as infile:
        messages = json.load(infile)
        messages.append(message)
    with open ('messages.json', 'w') as outfile: 
        json.dump(messages, outfile)



            



     



def authenticate_login():
    with open('users.json') as json_file:
        users = json.load(json_file)
        for user in users: 
            if name == user: 
                if users['pwdhash']== password: 
                    return "Success"
                else: 
                    return "Password incorrect"
            else: 
                return("Username not found!")
         
