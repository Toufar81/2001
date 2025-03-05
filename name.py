from flask import Flask, render_template, request

app = Flask(__name__)
name = []
you_score = 0
computer_score = 0

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        secund_name = request.form.get("second_name")
        name.append(first_name)
        name.append(secund_name)
        return render_template("welcom_start.html",first_name=first_name,secund_name=secund_name)
    else:
        return render_template("index.html")

@app.route('/game',methods=['GET','POST'])
def start():
    if request.method == 'POST':
        return render_template("game.html", first_name=name[0])
    else:
        return render_template("game.html",first_name=name[0])

@app.route('/rules',methods=['GET','POST'])
def stop():
    if request.method == 'POST':
        return render_template("rules.html")
    return render_template("welcom_start.html",first_name=name[0])

if __name__ == '__main__':
    app.run(debug=True)
