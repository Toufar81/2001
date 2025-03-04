from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        secund_name = request.form.get("second_name")
        return render_template("index.html",first_name=first_name,secund_name=secund_name)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
