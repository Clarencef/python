import turtle

def draw_square(turtle):
     for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)
        
def draw_triangle(turtle):
    turtle.left(60)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    draw_square(brad)
    angie = turtle.Turtle()
    angie.color('yellow')
    angie.circle(100)
    tim = turtle.Turtle()
    tim.color('white')
    draw_triangle(tim)
    big = turtle.Turtle()
    for i in range(1,37):
        draw_square(big)
        big.right(10)
    window.exitonclick()


draw_shape()
