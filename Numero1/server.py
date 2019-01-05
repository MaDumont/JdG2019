from flask import Flask, abort
import json
app = Flask(__name__)

ALIENS = []

def encode(data):
    data = json.dumps(data)
    data = data.replace('"', "'")
    data = data.replace('[', "/*")
    data = data.replace(']', "*/")
    data = data.replace('{', "^")
    data = data.replace('}', "&")

    return data

def decode(data):
    data = data.replace("'", '"')
    data = data.replace("/*", '[')
    data = data.replace("*/", ']')
    data = data.replace("^", '{')
    data = data.replace("&", '}')
    data = json.loads(data)

    return data

def find_alien(name):
    for alien in ALIENS:
        if alien['name'] == alien:
            return encode(alien)

@app.route("/api/alien", methods=['GET'])
def get_aliens():
    return encode(ALIENS)


@app.route("/api/alien", methods=['POST'])
def post_alien():
    data = decode(request.data)
    ALIENS.append(data)

    return encode({'ok': 200})


@app.route("/api/alien/name/<name>", methods=['GET'])
def get_alien(name):
    alien = find_alien(name)
    
    if alien:
        return encode(alien)
    
    abort(400) # selon la description

    
@app.route("/api/alien/name/<name>", methods=['DELETE'])
def delete_alien(name):
    remove_index = None
    
    for i in range(len(ALIENS)):
        if ALIENS[i]['name'] == name:
            remove_index = i
            break

    if remove_index is not None:
        del ALIENS[i]
        return ''
    else:
        abort(400)
        


@app.route("/api/alien/name/<name>", methods=['PUT'])
def put_alien(name):
    remove_index = None
    
    for i in range(len(ALIENS)):
        if ALIENS[i]['name'] == name:
            remove_index = i
            break

    if remove_index is not None:
        ALIENS[i] = decode(request.data)
        return ''
    else:
        abort(400)
