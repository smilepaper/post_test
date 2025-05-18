import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '這是你的 POST API！'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print("收到資料：", data)
    return jsonify({
        "message": "收到資料囉！",
        "yourData": data
    })

# 👇 這段非常關鍵
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render 會設定 PORT 環境變數
    app.run(host='0.0.0.0', port=port)
