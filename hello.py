from flask import Flask
from flask import request
import hashlib

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/', methods='GET')
def delete_students():
    if not request.args:
        return False
    signature = request.args['signature']
    timestamp = request.args['timestamp']
    nonce = request.args['nonce']
    echostr = request.args['echostr']
    # 自己的token
    token = "bqbs"  #这里改写你在微信公众平台里输入的token
    #字典序排序
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    #sha1加密算法

    #如果是来自微信的请求，则回复echostr
    if hashcode == signature:
        return echostr

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)