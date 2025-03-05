from flask import Flask, render_template, request
from itertools import zip_longest
import roll_cubes_finction

app = Flask(__name__)
name = []
you_score = 0
computer_score = 0
roll_count = 0

formatted_computer_score = list(str(computer_score).zfill(4))
formatted_you_score  = list(str(you_score).zfill(4))

    

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
    global you_score
    global computer_score
    global roll_count

    if request.method == 'POST':
        #count
        roll_count += 1
        formatted_roll_count = list(str(roll_count).zfill(2))

        #you
        you_result, you_cube1, you_cube2 = roll_cubes_finction.roll_cubes(10,roll_count)
        you_score += you_result
        formatted_you_cube1 = list(str(you_cube1).zfill(3))
        formatted_you_cube2 = list(str(you_cube2).zfill(3))
        formatted_you_score = list(str(you_score).zfill(4))

        #computer
        computer_result, computer_cube1, computer_cube2 = roll_cubes_finction.roll_cubes(10, roll_count)
        computer_score += computer_result

        formatted_computer_cube1 = list(str(computer_cube1).zfill(3))
        formatted_computer_cube2 = list(str(computer_cube2).zfill(3))
        formatted_computer_score = list(str(computer_score).zfill(4))
        return render_template("game.html", first_name=name[0],formatted_computer_score=formatted_computer_score,formatted_you_score=formatted_you_score,formatted_you_cube1=formatted_you_cube1,formatted_you_cube2=formatted_you_cube2,formatted_roll_count=formatted_roll_count,formatted_computer_cube1=formatted_computer_cube1,formatted_computer_cube2=formatted_computer_cube2)
    else:
        # count
        formatted_roll_count = (0,0)
        # you
        formatted_you_cube1 = (0,0,0)
        formatted_you_cube2 = (0,0,0)
        formatted_you_score = (0,0,0,0)
        # computer
        formatted_computer_cube1 = (0,0,0)
        formatted_computer_cube2 = (0,0,0)
        formatted_computer_score = (0,0,0,0)
        return render_template("game.html", first_name=name[0],formatted_computer_score=formatted_computer_score,formatted_you_score=formatted_you_score,formatted_you_cube1=formatted_you_cube1,formatted_you_cube2=formatted_you_cube2,formatted_roll_count=formatted_roll_count,formatted_computer_cube1=formatted_computer_cube1,formatted_computer_cube2=formatted_computer_cube2)

@app.route('/rules',methods=['GET','POST'])
def stop():
    if request.method == 'POST':
        return render_template("rules.html")
    return render_template("welcom_start.html",first_name=name[0])

if __name__ == '__main__':
    app.run(debug=True)
