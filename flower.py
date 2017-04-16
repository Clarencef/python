import turtle

def test(drawer):
    drawer.forward(100)
    drawer.right(45)
    drawer.forward(25)
    drawer.right(90)
    drawer.forward(25)
    drawer.right(60)
    drawer.forward(100)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")
    drawer = turtle.Turtle()
    drawer.color('white')
    for i in range(1,37):
        test(drawer)
        drawer.right(10)
    drawer.left(90)
    drawer.forward(300)
    window.exitonclick()

draw_flower()
