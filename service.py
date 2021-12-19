from flask import Flask, request

app = Flask(__name__)


# GET function: Runs hello world on your local host
@app.route("/")
def hello_world():
    return "<p>This is a test for Hello, World!</p>"


# Users Functionality
@app.route("/users/", methods=['GET', 'POST', 'PUT'])
def users():

    # POST method for
    if request.method == 'POST':
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        return "<p>new_user_added " + first_name + " " + last_name + "</p>"


if __name__ == "__main__":
    app.run()
