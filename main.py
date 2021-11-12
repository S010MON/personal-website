from flask import Flask, request

app = Flask(__name__)

# GET function: Runs hello world on your local host
@app.route("/")
def hello_world():
    return "<p>This is a test for Hello, World!</p>"


# GET function: Adding a sub-level to the root of the URL
@app.route("/about/")
def about():
    return "<p>About the author</p>"


# GET function: Taking in a parameter using the URL
@app.route("/square/<number>", methods=['GET'])
def square(number):
    number = int(number)        # This step is required to change the type to an Integer
    number = number * number
    return "<p>" + str(number) + "</p>"


# Users Functionality
@app.route("/users/", methods=['POST'])
def users():

    # POST method for
    if request.method == 'POST':
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        return "<p>new_user_added " + first_name + " " + last_name + "</p>"


if __name__ == "__main__":
    app.run()
