points = [(1, 3), (4, 8), (5, 12)]
distances = []

def euclideanDistance(x, y):
    dx= x[0]-y[0]
    dy= x[1]-y[1]
    return (dx **2 +dy ** 2) ** (1/2)


for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)

def minDistances(distances):
    min_distance = distances[0]
    for i in distances:
        if i < min_distance:
            min_distance= i
    return min_distance


min_distance= minDistances(distances)

print("Hesaplanan Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)