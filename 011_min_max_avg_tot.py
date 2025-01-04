def min_max_avg_tot(x, y, z):
    minimum = maximum = x
    if y < minimum:
        minimum = y
    if z < minimum:
        minimum = z
    if y > maximum:
        maximum = y
    if z > maximum:
        maximum = z
    total = x+y+z
    average = total/3
    return minimum, maximum, average, total

min_max_avg_tot(5, 6, 7)
