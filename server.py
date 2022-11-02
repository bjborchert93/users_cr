from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/user")

@app.route('/user')
def get_all_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

@app.route('/new_user')
def new_user():
    return render_template("create.html")

@app.route('/create_user', methods=['POST'])
def create_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    User.save(data)

    return redirect('/user')
            
if __name__ == "__main__":
    app.run(debug=True)