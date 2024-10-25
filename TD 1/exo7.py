import math
# exo 7
print('----------exo7 started---------')

x1, y1, z1 = map(float, input("Enter the coordinates of the first point (x1, y1, z1): ").split())
x2, y2, z2 = map(float, input("Enter the coordinates of the second point (x2, y2, z2): ").split())
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
print(f"The distance between the two points is: {distance:.2f}")

print('----------exo7 finished---------')