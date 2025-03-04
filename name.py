from flask import Flask, render_template, request

app = Flask(__name__)
name = []
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

@app.route('/start',methods=['GET','POST'])
def start():

    return "Tlacitko bylo stisknuto"
if __name__ == '__main__':
    app.run(debug=True)
