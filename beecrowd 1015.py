
import math
p1 = list(map(float,input().split(" ")))
p2 = list(map(float,input().split(" ")))

c1 = ((p2[0])-(p1[0]))**2
c2 = ((p2[1])-(p1[1]))**2
math = math.sqrt(c1+c2)
print(f"{math:.4f}")

"""
import math

p1 = list(map(float, input().split(" ")))
p2 = list(map(float, input().split(" ")))

c1 = (p2[0] - p1[0]) ** 2
c2 = (p2[1] - p1[1]) ** 2
distance = math.sqrt(c1 + c2)
print(f"{distance:.4f}")
"""
