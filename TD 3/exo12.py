# Example
"""
1
11
121
1331
14641
"""
# Code
n = int(input('entrez la valuer de N: '))

pascal_triangle = [[1]] # Triangle Base

for i in range(n):
    pascal_row = [1] # row Edges
    for j in range(len(pascal_triangle[i]) - 1):
        # Add adjacent elements From the previous row
        pascal_row.append(pascal_triangle[i][j] + pascal_triangle[i][j + 1]) 

    pascal_row.append(1) # row Edges
    pascal_triangle.append(pascal_row) # Append The row To the Triangle

for row in pascal_triangle: # Printing row by row From The Triangle
    print(row)

