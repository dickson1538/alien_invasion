import random

range_star_x = (0, 800)
range_star_y = (0, 800)

x_values = []
y_values = []

for i in range(10):
    if x_values == 10:
        break
    else:
        x = random.randrange(*range_star_x)
        y = random.randrange(*range_star_y)
        x_values.append(x)
        y_values.append(y)

for i in range(len(x_values)):
    coordinates = (x_values[i], y_values[i])


