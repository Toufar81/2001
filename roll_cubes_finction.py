import random

def roll_cubes(cube1_set,cube2_set,score):
    print(f"Debug Roll cube c1-{cube1_set} c2-{cube2_set}")
    result_score =0

    cube1_res = random.randint(1,cube1_set)
    cube2_res = random.randint(1,cube2_set)
    score_res = cube1_res + cube2_res + score
    if cube1_res == 7 or cube2_res == 7:
        score_result = int(round(score_res / 7, 0))
        result_score = score_result
    elif cube1_res == 11 or cube2_res == 11:
        score_result = score_res * 11
        result_score = score_result
    else:
        result_score = score_res

    return result_score,cube1_res,cube2_res

def computer_rand_cube():
    cubes_list = [3, 4, 6, 8, 10, 12, 20, 50]
    rand_cube = random.choice(cubes_list)
    print(f"Debug computer_rand_cube {rand_cube}")
    return rand_cube