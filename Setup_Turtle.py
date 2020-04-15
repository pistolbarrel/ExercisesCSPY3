'''
program to investigate creation of objects, creation of tuples, refactoring code, turtle and screen objects,

'''


def setup_turtle() -> object:
    import turtle
    window = turtle.Screen()
    tess = turtle.Turtle()
    return(window,tess)

# window, tess = setup_turtle()

window,tess = setup_turtle()
print(tess)
# print(window, tess)

tess.fd(100)
# print(w,t)
window.mainloop()
