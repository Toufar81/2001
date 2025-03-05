import random

def roll_cubes(cube = 6,roll_count = 1):
    result_score =0
    if roll_count == 1:
        cube1 = random.randint(1,6)
        cube2 = random.randint(1,6)
        result_score = cube1 + cube2
        return result_score,cube1,cube2
    else:
        cube1 = random.randint(1,cube)
        cube2 = random.randint(1,cube)
        roll_score = cube1 + cube2
        if cube1 == 7 or cube2 == 7:
            result_score = int(round(roll_score / 7, 0))
        elif cube1 == 11 or cube2 == 11:
            result_score = roll_score * 11
        else:
            result_score = roll_score
        return result_score,cube1,cube2