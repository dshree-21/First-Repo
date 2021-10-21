import random

MIN_NUM = 1
MAX_NUM = 10
nb_ques = 4


def ask_question():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    o = random.randint(0, 1)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    answer_str = input(f"Compute: {a} {operator_str} {b} = ")
    answer_int = int(answer_str)
    compute = a+b
    if o == 1:
        compute = a*b
    if answer_int == compute:
        return True

    return False


nb_points = 0
for i in range(0, nb_ques):
    print(f"Question no. {i+1} out of {nb_ques}: ")
    if ask_question():
        print("Right answer")
        nb_points += 1
    else:
        print("Wrong Answer ")
    print()


print(f"Your points : {nb_points} out of {nb_ques} ")
avg = int(nb_ques/2)
if nb_points == nb_ques:
    print("Excellent!")
elif nb_points == 0:
    print("Improve your maths!")
elif nb_points > avg:
    print("Good!")
else:
    print("You can do better !")
