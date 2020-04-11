def setup_turtle() -> object:
    import turtle
    window = turtle.Screen()
    tess = turtle.Turtle()
    return(window,tess)


window, tess = setup_turtle()
print(window, tess)

tess.fd(100)
# print(w,t)
window.mainloop()
