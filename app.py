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
    with open('tasks.json') as json_file:
        tasks = json.load(json_file)
        for task in tasks:
            if task['initiatior'] == user: 
                reward = task["reward"]
            



     



def authenticate_login():
    with open('users.json') as json_file:
        users = json.load(json_file)
        for user in users: 
            if name == user: 
                if data['user']== password: 
                    return "Success"
                else: 
                    return "Password incorrect"
            else: 
                return("Username not found!")
         
