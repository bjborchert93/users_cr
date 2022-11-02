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
    return render_template("read_all.html", users=users)

@app.route('/user/new')
def new_user():
    return render_template("create.html")

@app.route('/user/create', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/user')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {"id": id}
    return render_template("edit.html", user=User.get_user(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {"id": id}
    return render_template("read_one.html", user=User.get_user(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/user')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {'id': id}
    User.destroy(data)
    return redirect('/user')

if __name__ == "__main__":
    app.run(debug=True)