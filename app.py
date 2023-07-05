from flask import Flask  # 導入模組Flask
app = Flask(__name__)  # 呼叫Flask的固定用法


@app.route("/")  # 裝飾器@app.route，之後會解釋
def hello():
    return "Hello World!"


if __name__ == "__main__":  # 如果主程式執行
    app.run()  # 啟動伺服器