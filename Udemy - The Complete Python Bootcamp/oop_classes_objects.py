# from turtle import Turtle, Screen

# my_screen = Screen()
# donatello = Turtle()


# my_screen.exitonclick()

# OOP DEFINING CLASSES AND OBJECTS
class Robot:
    """THIS CLASS IMPLEMENTS A ROBOT"""

    def __init__(self, name, year):
        self.name = name
        self.year = year


r1 = Robot("R1", 2023)

print(r1.__dict__)
