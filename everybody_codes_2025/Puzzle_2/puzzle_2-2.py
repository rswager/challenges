from knight_step import KnightStep

def test_point(point_in: KnightStep):
    check_result = KnightStep([0,0])
    result = True
    cycle_broke = -1
    for i in range(100):
        # Multiply the results by iteslf
        check_result = check_result * check_result

        # divide the resulbe by [100_000,100_000]
        check_result = check_result / [100_000, 100_000]

        # add the coordinates of the point under examiniation
        check_result = check_result + point_in
        if abs(check_result.value[0]) > 1_000_000 or abs(check_result.value[1]) > 1_000_000:
            result = False
            cycle_broke = i
            break
    return result, cycle_broke, check_result

#A=KnightStep([35300,-64910])
A=KnightStep([-21703,67997])
top_left_corner = A

# Calculate the bottom right corner
bottom_right_corner = A + [1_000, 1_000]

x1 = top_left_corner.value[0]
y1 = top_left_corner.value[1]
x2 = bottom_right_corner.value[0]
y2 = bottom_right_corner.value[1]

sub_division_x = int((x2-x1)/100)
sub_division_y = int((y2-y1)/100)

# sub_divide the board
current_pos = KnightStep([x1, y1])
places = []
while current_pos.value[1] <= y2:
    row = []
    while current_pos.value[0] <= x2:
        row.append(current_pos)
        current_pos = current_pos + [sub_division_x, 0]
    places.append(row)
    current_pos = current_pos + [0, sub_division_y]
    current_pos.value[0] = x1

# Check values count # of engravings
engrave = 0
for row in places:
    for points in row:
        result, cycle_broke, check_result = test_point(points)
        engrave += 1 if result else 0

print(engrave)

