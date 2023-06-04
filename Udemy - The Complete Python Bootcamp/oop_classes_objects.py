# from turtle import Turtle, Screen

# my_screen = Screen()
# donatello = Turtle()


# my_screen.exitonclick()

# OOP DEFINING CLASSES AND OBJECTS
class Robot:
    """THIS CLASS IMPLEMENTS A ROBOT"""
    population = 0

    def __init__(self, name, year):  # CONSTRUCTOR
        self.name = name
        self.year = year
        Robot.population += 1


r1 = Robot("R1", 2023)

print(r1.__dict__)
print(Robot.population)
