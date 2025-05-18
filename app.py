from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print("接收到資料：", data)
    return jsonify({
        "message": "資料收到囉！",
        "you_sent": data
    })

@app.route('/', methods=['GET'])
def home():
    return "這是你的 POST 測試 API！"
