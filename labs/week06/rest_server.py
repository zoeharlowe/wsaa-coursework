from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

# get all films
@app.route('/films', methods=['GET'])
def getall():
    return "get all"

# find a film by id
@app.route('/films/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"

# create a new film
@app.route('/films', methods=['POST'])
def create():
    # read json from the body
    jsonstring = request.json
    return f"create {jsonstring}"

# update a film by id
@app.route('/films/<int:id>', methods=['PUT'])
def update(id):
    # read json from the body
    jsonstring = request.json
    return f"update {id} {jsonstring}"

# delete a film by id
@app.route('/films/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == '__main__':
    app.run(debug=True)