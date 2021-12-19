from flask import Flask, request
import controller

app = Flask(__name__)


# GET function: Runs hello world on your local host
@app.route("/")
def hello_world():
    return "<p>This is a test for Hello, World!</p>"


# Users Functionality
@app.route("/users/", methods=['GET', 'POST', 'PUT'])
def users():

    # GET method for
    if request.method == 'GET':
        type = request.json['type']
        param = request.json['param']

        if type == "user_id":
            response = controller.get_user_by_id(param)
        elif type == "email":
            response = controller.get_user_by_email(param)
        else:
            response = controller.get_404()
        return response

    # POST method for
    if request.method == 'POST':
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        date_of_birth = request.json['date_of_birth']
        email = request.json['email']
        phone = request.json['phone']
        response = controller.add_user(first_name, last_name, date_of_birth, email, phone)
        return response


if __name__ == "__main__":
    app.run()
