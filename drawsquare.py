import turtle

def draw_square(brad):
    i = 0
    while (i < 4):
        brad.speed(10)
        brad.forward(100)
        brad.right(90)
        i = i + 1

def draw_circle(angie):    
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_art():        
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    i = 0
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()


