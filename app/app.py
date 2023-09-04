import random
import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

win_count = 20
lose_count = 30


@app.route('/', methods=['GET', 'POST'])
def index():
    global win_count, lose_count
    if request.method == 'POST':
        result = 'ハズレ'
        if win_count > 0:
            if random.random() < 0.4:
                result = 'アタリ'
                win_count -= 1
            else:
                lose_count -= 1
        elif lose_count > 0:
            result = 'ハズレ'
            lose_count -= 1
        print(f"現在のアタリ残数：{win_count}\n現在のハズレ残数：{lose_count}")
        return render_template('result.html', title="くじ引き-くじの結果", result=result)
    else:
        return render_template('index.html', title="くじ引き", win_count=win_count, lose_count=lose_count)


@app.route('/reset', methods=["POST"])
def reset():
    global win_count, lose_count
    win_count = 20
    lose_count = 30
    return redirect(url_for("index"))


@app.route('/set', methods=['GET', 'POST'])
def set():
    global win_count, lose_count
    if request.method == "GET":
        return render_template("set.html", win_count=win_count, lose_count=lose_count)
    else:
        win_count = int(request.form.get("win_count"))
        lose_count = int(request.form.get("lose_count"))
        return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
