from flask import Flask, render_template, request

app = Flask(__name__)  # __name__ 代表目前執行的模組


@app.route("/")  # 函式的裝飾(Decorator)： 以函式為基礎，提供附加的功能
def home():
    return render_template("index.html")


@app.route("/test")  # 當網站連接到根目錄底下的test路徑，執行test函式
def test():
    return "This is a test."


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"


@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    return process_query(q)


if __name__ == "__main__":
    app.run(debugger=True)
