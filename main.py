from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "first_name": "James",
        "last_name": "Butt",
        "company_name": "Benton, John B Jr",
        "city": "New Orleans",
        "state": "LA",
        "zip": 70116,
        "email": "jbutt@gmail.com",
        "web": "http://www.bentonjohnbjr.com",
        "age": 70
    },
    {
        "id": 2,
        "first_name": "Josephine",
        "last_name": "Darakjy",
        "company_name": "Chanay, Jeffrey A Esq",
        "city": "New Orleans",
        "state": "LA",
        "zip": 70116,
        "email": "jbjohndoe@gmail.com",
        "web": "http://www.bentonjobjr.com",
        "age": 60
    },
    {
        "id": 3,
        "first_name": "Josephine",
        "last_name": "Darakjy",
        "company_name": "Chanay, Jeffrey A Esq",
        "city": "New Orleans",
        "state": "LA",
        "zip": 70116,
        "email": "jbjohndoe@gmail.com",
        "web": "http://www.bentonjobjr.com",
        "age": 60
    }
]


@app.route('/')
def index():
    return "welcome to the API section"


@app.route("/users", methods=['GET'])
def get():
    return jsonify({'users': users})


@app.route("/users/<int:id>", methods=['GET'])
def get_employee(id):
    return jsonify({'users': users[id]})


@app.route("/users", methods=['POST'])
def create():
    user = {
        "id": 4,
        "first_name": "John",
        "last_name": "Doe",
        "company_name": "FB, Jeffrey A Esq",
        "city": "New York",
        "state": "CA",
        "zip": 70116,
        "email": "johndoe@gmail.com",
        "web": "http://www.bentonjobjr.com",
        "age": 40
    }
    users.append(user)
    return jsonify({'Created': user})


@app.route("/users/<int:id>", methods=['PUT'])
def user_update(id):
    users[id]['email'] = "jadjbsbb@ddsd.com"
    return jsonify({'users': users[id]})

@app.route("/users/<int:id>", methods=['DELETE'])
def delete(id):
    users.remove(users[id])
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(debug=True)
