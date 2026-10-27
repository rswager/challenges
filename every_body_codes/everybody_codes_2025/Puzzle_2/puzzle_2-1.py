"""
A=[160,50]
"""
from knight_step import KnightStep

sets = [[1,1],[2,2],[2,5],[3,7],[-2,5],[10,-1],[-1,-2],[-3,-4],]
knight_steps = [KnightStep(set) for set in sets]

print("ADD")
print(knight_steps[0] + knight_steps[1])
print(knight_steps[2] + knight_steps[3])
print(knight_steps[4] + knight_steps[5])
print(knight_steps[6] + knight_steps[7])

print("MULTIPLY")
print(knight_steps[0] * knight_steps[1])
print(knight_steps[2] * knight_steps[3])
print(knight_steps[4] * knight_steps[5])
print(knight_steps[6] * knight_steps[7])

print("DIVISION")
print([10, 12] / knight_steps[1])
print(KnightStep([11, 12]) / KnightStep([3, 5]))
print(KnightStep([-10, -12]) / KnightStep([2, 2]))
print(KnightStep([-11, -12]) / KnightStep([3, 5]))

R = KnightStep([0, 0])
std_10_10 = [10, 10]
# A = KnightStep([25, 9])
A = KnightStep([160,50])

print("CYCLE I")
R = R * R
print(R)
R = R / std_10_10
print(R)
R = R + A
print(R)

print("CYCLE II")
R = R * R
print(R)
R = R / std_10_10
print(R)
R = R + A
print(R)

print("CYCLE III")
R = R * R
print(R)
R = R / std_10_10
print(R)
R = R + A
print(R)
