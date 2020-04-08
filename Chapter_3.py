def exercise_1():
    for i in range(1000):
        print(i, "We Like Python's Turtles")


# def exercise_2():


def exercise_3():
    for f in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]:
        print("One of the months of the year is ", f)


# def exercise_4():


def exercise_5():
    xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

    print("numbers: ")
    for i in xs:
        print(i, end="\n")

    print("squares: ")
    for i in xs:
        print(i, i ** 2)

    print("sum total: ")
    total = 0
    for i in xs:
        total = total + i

    print(total)

    print("product1:")
    xy = [3, 10, 4]

    total = xy[0]
    for i in range(2):
        total = total * xy[i + 1]
    print(total)

    total = xy[0]
    for i in range(len(xy) - 1):
        total = total * xy[i + 1]
    print(total)

    print("product2: ")
    print(xs)
    total = xs[0]
    for i in range(len(xs) - 1):
        total = total * xs[i + 1]
    print(total)


def exercise_6():
    import turtle
    bob = turtle.Turtle()
    wn = turtle.Screen()
    polygon(bob,8)
    # wn.mainloop()


def polygon(t,num_sides):

    for i in range(num_sides):
        t.fd(100)
        t.lt(360 / num_sides)



def exercise_7():
    import turtle
    bob = turtle.Turtle()
    wn = turtle.Screen()

    pirate_steps = [160,-43,270,-97,-43,200,-940,17,-86]
    for i in (pirate_steps):
        bob.lt(i),
        bob.fd(100)

    wn.mainloop()


'''
def exercise_8():


def exercise_9():


def exercise_10():


def exercise_11():


def exercise_12():


def exercise_13():


def exercise_14():


def exercise_15():


'''

exercise_7()
