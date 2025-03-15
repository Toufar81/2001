from flask import Flask, render_template, request
import roll_cubes_finction

app = Flask(__name__)

name = []
you_score = 0
computer_score = 0
roll_count = 0
get_tube_n1_int = None
get_tube_n2_int = None
messages_list = list()
win_score = None

formatted_computer_score = list(str(computer_score).zfill(4))
formatted_you_score  = list(str(you_score).zfill(4))

    

@app.route('/',methods=['GET','POST'])
def index():
    global win_score
    if request.method == 'POST':
        win_score = None
        first_name = request.form.get("first_name")
        secund_name = request.form.get("second_name")
        name.append(first_name)
        name.append(secund_name)
        print(f"debug index win_score: {win_score}")
        return render_template("welcom_start.html",first_name=first_name,secund_name=secund_name,win_score=win_score)
    else:
        return render_template("index.html")

@app.route('/game',methods=['GET','POST'])
def start():
    global you_score
    global computer_score
    global roll_count
    global get_tube_n1_int
    global get_tube_n2_int
    global messages_list

    if request.method == 'POST':
        messages_list.clear()
        # count
        roll_count += 1

        if get_tube_n1_int == None and get_tube_n2_int == None and roll_count==1:
            # you
            you_result, you_cube1, you_cube2 = roll_cubes_finction.roll_cubes(6, 6,you_score)
            you_score = you_result
            # computer
            computer_result, computer_cube1, computer_cube2 = roll_cubes_finction.roll_cubes(
                6, 6,computer_score)
            computer_score = computer_result
        elif get_tube_n1_int != None and get_tube_n2_int != None:
            #you
            you_result, you_cube1, you_cube2 = roll_cubes_finction.roll_cubes(get_tube_n1_int,get_tube_n2_int,you_score)
            you_score = you_result
            #computer
            computer_result, computer_cube1, computer_cube2 = roll_cubes_finction.roll_cubes(roll_cubes_finction.computer_rand_cube(),roll_cubes_finction.computer_rand_cube(),computer_score)
            computer_score = computer_result

            if you_cube1 == 7 or you_cube2 == 7 or computer_cube1 == 7 or computer_cube2 == 7:
                messages_list.append("It was a 7, what bad luck")

            if computer_cube1 == 11 or computer_cube2 == 11 or you_cube1 == 11 or you_cube2 == 11:
                messages_list.append("Hooray, what luck 11")
            if roll_count % 2 == 0:
                if computer_score > you_score:
                    messages_list.append(f" So far, the computer is winning")
                elif computer_score == you_score:
                    messages_list.append(f" So far it's a draw")
                elif computer_score < computer_score:
                    messages_list.append(f" For now, {name} is winning")
        else:
            if get_tube_n1_int == None and get_tube_n2_int == None:
                messages_list.append(f" You did not enter both dice")
            elif get_tube_n1_int == None:
                messages_list.append(f" You did not enter the cube 1")
            elif get_tube_n2_int == None :
                messages_list.append(f" You did not enter the cube 2")
            you_cube1 =0
            you_cube2 = 0
            computer_cube1 = 0
            computer_cube2 = 0
            roll_count -= 1


        formatted_roll_count = list(str(roll_count).zfill(2))

        formatted_you_cube1 = list(str(you_cube1).zfill(3))
        formatted_you_cube2 = list(str(you_cube2).zfill(3))
        formatted_you_score = list(str(you_score).zfill(4))

        formatted_computer_cube1 = list(str(computer_cube1).zfill(3))
        formatted_computer_cube2 = list(str(computer_cube2).zfill(3))
        formatted_computer_score = list(str(computer_score).zfill(4))
        get_tube_n1_int = None
        get_tube_n2_int = None
        if you_score >= win_score:
            winer = name[0]
            return render_template("win.html", winer=winer, you_score=you_score, computer_score=computer_score)
        elif computer_score >= win_score:
            winer =  "Computer"
            return render_template("win.html",winer=winer, you_score=you_score, computer_score=computer_score)
        else:
            return render_template("game.html", first_name=name[0],formatted_computer_score=formatted_computer_score,formatted_you_score=formatted_you_score,formatted_you_cube1=formatted_you_cube1,formatted_you_cube2=formatted_you_cube2,formatted_roll_count=formatted_roll_count,formatted_computer_cube1=formatted_computer_cube1,formatted_computer_cube2=formatted_computer_cube2,messages_list=messages_list,roll_count=roll_count)
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
        return render_template("game.html", first_name=name[0],formatted_computer_score=formatted_computer_score,formatted_you_score=formatted_you_score,formatted_you_cube1=formatted_you_cube1,formatted_you_cube2=formatted_you_cube2,formatted_roll_count=formatted_roll_count,formatted_computer_cube1=formatted_computer_cube1,formatted_computer_cube2=formatted_computer_cube2,messages_list=messages_list,roll_count=roll_count)

@app.route('/rules',methods=['GET','POST'])
def stop():
    if request.method == 'POST':
        return render_template("rules.html")
    print(f"Debug win_score: {win_score}")
    return render_template("welcom_start.html",first_name=name[0],win_score=win_score)

@app.route('/get_tube_n1',methods=['POST'])
def get_tube_n1():
    global get_tube_n1_int
    get_tube_n1_int = (request.form.get("get_tube_n1"))
    if get_tube_n1_int != None:
        get_tube_n1_int = int(get_tube_n1_int)
    else:
        get_tube_n1_int = None
    print(f"Debug getcube {get_tube_n1_int} {type(get_tube_n1_int)}")

    return '', 204

@app.route('/get_tube_n2',methods=['POST'])
def get_tube_n2():

    global get_tube_n2_int
    get_tube_n2_int = (request.form.get("get_tube_n2"))
    if get_tube_n2_int != None:
        get_tube_n2_int = int(get_tube_n2_int)
    else:
        get_tube_n2_int = None

    print(f"Debug getcube {get_tube_n2_int} {type(get_tube_n2_int)}")
    return '', 204
@app.route('/get_win_score',methods=["GET",'POST'])
def get_win_score():
    global you_score
    global computer_score
    global roll_count
    global messages_list
    if request.method == 'POST':
        global win_score
        win_score = int(request.form.get("win_score"))
        print(f"Debug c: {win_score}")
        return render_template("welcom_start.html",first_name=name[0],win_score=win_score)
    else:
        win_score = None
        you_score = 0
        computer_score = 0
        roll_count = 0
        messages_list = list()
        print(f"Debug get_win_score: {win_score}")
        return render_template("welcom_start.html", first_name=name[0], win_score=win_score)

if __name__ == '__main__':
    app.run(debug=True)
