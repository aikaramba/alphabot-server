from flask import Flask, jsonify, request
from AlphaBot import AlphaBot

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
    if request.args.get('dc') >= 0 and request.args.get('dc') <= 100:
        alphaBot.setPWMA(request.args.dc)
    return jsonify(response)

@app.route('/set_pwmb', methods=['GET'])
def setPWMB():
    if request.args.get('dc') >= 0 and request.args.get('dc') <= 100:
        alphaBot.setPWMB(request.args.get('dc'))
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000, debug=False)
