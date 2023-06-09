import numpy as np

points = np.array([[-1, 0], [2, 2], [2, 0]])
concentrations = np.array([16.3, 12.4, 13.7])

def variogram(h):
    if h < 2.5:
        return 2.4 * h - 0.128 * h**3
    else:
        return 4

def distance(point_a, point_b):
    return np.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

point_A = np.array([0, 0])

distances = [distance(point_A, point) for point in points]

gamma = [0.5 * (concentrations[i] - concentrations[j])**2 for i in range(3) for j in range(i+1, 3) if distances[i] == distances[j]]

h_range = np.arange(0, 5, 0.1)
theoretical_gamma = [variogram(h) for h in h_range]

if distance(point_A, points[0]) < 2.5:
    y_A = variogram(distance(point_A, points[0]))
else:
    y_A = 4
    
print("The estimated concentration of thorium at point A is:", y_A, "ppm")
