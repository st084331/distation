import csv
from math import sqrt

x = []
y = []
z = []

with open('Координаты.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(int(row['X']))
        y.append(int(row['Y']))
        z.append(int(row['Z']))

print(2**2)

for point in range(100):
    neighbor = [0, 0, 0, 0]
    n_range = float('inf')
    for j in range(len(x)):
        if(point != j):
            p_range = sqrt(((x[point] - x[j])**2) + ((y[point] - y[j])**2) + ((z[point] - z[j])**2))
            if(p_range < n_range):
                n_range = p_range
                neighbor = [j, x[j], y[j], z[j]]
    print("The neighbor of point number", point, "is point number", neighbor[0], "with coordinates",
          neighbor[1], neighbor[2], neighbor[3], "and distance between them equals", n_range)