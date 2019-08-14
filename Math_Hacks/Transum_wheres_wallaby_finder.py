import math


def increment():
    global a_var
    global b_var
    global search_quantity
    global search_limit
    global is_completed

    if search_quantity > search_limit:
        is_completed = True

    search_quantity = search_quantity + 1
    a_var = a_var + 1
    if a_var > 20:
        b_var = b_var + 1
        a_var = 0


def find_wallaby(distance):
    global a_var
    global b_var
    global search_quantity
    global search_limit
    global is_completed

    to_round = distance ** 2
    goal = round(to_round)
    print("Squared '{original}' to '{new}' and rounded to '{rounded}'"
          .format(original=distance, new=to_round, rounded=goal))

    # Iteration Progress
    a_var = 0
    b_var = 0
    search_quantity = 0
    search_limit = 500
    completed_list = []
    is_completed = False

    while is_completed is False:
        if (a_var ** 2) + (b_var ** 2) == goal:
            completed_equation = "{sqra}, {sqrb} OR {sqrb}, {sqra}".format(sqra=round(a_var), sqrb=round(b_var))
            message = "Triangle found! It is {equation_here}. Adds up to {total}".format(equation_here=completed_equation, total=((a_var ** 2) + (b_var ** 2)))
            print(message)
            completed_list.append(message)
            increment()

        else:
            increment()

            wrong_equation = "{sqra}, {sqrb} OR {sqrb}, {sqra}".format(sqra=a_var, sqrb=b_var)
            print("Triangle '{wrong_equation}' incorrect. Adds up to {total}"
                  .format(wrong_equation=wrong_equation, total=((a_var ** 2) + (b_var ** 2))))

    print("All Correct:")
    for row in completed_list:
        print(row)


find_wallaby(7.07)
