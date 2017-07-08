from flask import Flask, jsonify, request
from AlphaBot import AlphaBot
import os

alphaBot = AlphaBot();
alphaBot.stop();
response = {'status': u'ok'};

app = Flask(__name__)

@app.route('/forward', methods=['GET'])
def forward():
    alphaBot.forward()
    return jsonify(response)

@app.route('/backward', methods=['GET'])
def backward():
    alphaBot.backward()
    return jsonify(response)

@app.route('/left', methods=['GET'])
def left():
    alphaBot.left()
    return jsonify(response)

@app.route('/right', methods=['GET'])
def right():
    alphaBot.right()
    return jsonify(response)

@app.route('/stop', methods=['GET'])
def stop():
    alphaBot.stop()
    return jsonify(response)

@app.route('/set_pwma', methods=['GET'])
def setPWMA():
    dcValue = request.args.get('dc')
    if dcValue >= 10 and dcValue <= 90:
        alphaBot.setPWMA(dcValue)
    return jsonify(response)

@app.route('/set_pwmb', methods=['GET'])
def setPWMB():
    dcValue = request.args.get('dc')
    if dcValue >= 10 and dcValue <= 90:
        alphaBot.setPWMB(dcValue)
    return jsonify(response)

@app.route('/reboot', methods=['GET'])
def reboot():
    os.system('reboot')
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=False)
