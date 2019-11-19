#!flask/bin/python
from flask import Flask, redirect, url_for,request, jsonify
import json
import requests
import os

app = Flask(__name__)

ip_saida = os.environ["IP_REDIRECT"]
running_port = os.environ["R_PORT"]

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    headers = request.headers
    data = request.get_json()
    if request.method == 'POST':
        req = requests.post('http://' + ip_saida + ':' + str(running_port) + '/' + path, headers=headers, json=data)
        return req.content,req.status_code
    
    elif request.method == 'PUT':
        req = requests.put('http://' + ip_saida + ':' + str(running_port) + '/' + path, headers=headers, json = data)
        return req.content,req.status_code
    
    elif request.method == 'DELETE':
        req = requests.delete('http://' + ip_saida + ':' + str(running_port) + '/' + path)
        return req.content,req.status_code
    
    elif request.method == 'GET':
        req = requests.get('http://' + ip_saida + ':' + str(running_port) + '/' + path)
        answer = json.loads(req.content.decode('utf-8'))
        return jsonify(answer),req.status_code

@app.route('/healthcheck')
def hc():
    return '',200


if __name__ == '__main__':
    app.run('localhost',port=running_port)