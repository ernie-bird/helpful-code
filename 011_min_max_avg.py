def min_max_avg(x, y, z):
    minimum = maximum = x
    if y < minimum:
        minimum = y
    if z < minimum:
        minimum = z
    if y > maximum:
        maximum = y
    if z > maximum:
        maximum = z
    average = (x+y+z)/3
    return minimum, maximum, average

min_max_avg(5, 6, 7)
