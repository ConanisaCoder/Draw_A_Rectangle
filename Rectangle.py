import turtle
print("Enter the Length and Width of Rectangle in Pixels")
length = int(input(" The Length in px: "))
heigth = int(input("The Heigth in px: "))
Screen = turtle.Screen()
rectangle = turtle.Turtle()
for i in range(0,2,1):
    rectangle.forward(heigth)
    rectangle.left(90)
    rectangle.forward(length)
    rectangle.left(90)
