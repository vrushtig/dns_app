import socket
import pickle
from flask import Flask, request
import logging as log
app = Flask(__name__)
BUFFER_SIZE = 1024

@app.route('/')
def introduction_FS():
    return "Welcome to Fibonacci Server (FS)"

def get_FIBON(n):
    if n < 0:
        raise ValueError("n should be greater than 0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return get_FIBON(n - 1) + get_FIBON(n - 2)


@app.route('/fibonacci')
def fibonacci():
    n = int(request.args.get('number'))
    return str(get_FIBON(n))


@app.route('/register', methods=['PUT'])
def register():
    body = request.json
    if not body:
        raise ValueError("body is None")
    hostname = body["hostname"]
    fs_ip    = body["fs_ip"]
    as_ip    = body["as_ip"]
    as_port  = body["as_port"]
    ttl      = body["ttl"]
    msg_bytes = pickle.dumps(((hostname, fs_ip, "A", ttl)))
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(msg_bytes, (as_ip, as_port))
    return "Congratulations, Registeration is complete!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=9090,
            debug=True)