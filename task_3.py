class Angle:

    def __init__(self, value):
        self.value = value

    def calculator(self):
        if self.value == 360:
            return 0
        if self.value >= 360:
            return self.value % 360
        else:
            return abs(self.value)


angle_example1 = Angle(270+270)
angle_example2 = Angle(90-180)
angle_example3 = Angle(90*2)
print("Angle example 1:")
print(angle_example1.calculator())
print("Angle example 2:")
print(angle_example2.calculator())
print("Angle example 3:")
print(angle_example3.calculator())
