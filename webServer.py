#!flask/bin/python
from flask import Flask, redirect, url_for,request, jsonify
import requests
import os

app = Flask(__name__)

ip_saida = os.environ["IP_REDIRECT"]
running_port = os.environ["R_PORT"]
print(ip_saida)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path, methods = ['GET', 'POST', 'PUT', 'DELETE']):
    print("entrou na função")
    print(ip_saida + ':' + str(running_port) + '/' + path)
    if request.method == 'POST':
        req = requests.post('http://' + ip_saida + ':' + str(running_port) + '/' + path, data = request.get_json())
        return req.content
    elif request.method == 'PUT':
        req = requests.put('http://' + ip_saida + ':' + str(running_port) + '/' + path, data = request.get_json())
        return req.content
    elif request.method == 'DELETE':
        req = requests.delete('http://' + ip_saida + ':' + str(running_port) + '/' + path)
        return req.content
    elif request.method == 'GET':
        print("entrou no GET")
        req = requests.get('http://' + ip_saida + ':' + str(running_port) + '/' + path)
        return req.content

@app.route('/healthcheck')
def hc():
    return '',200


if __name__ == '__main__':
    app.run('0.0.0.0',port=running_port)