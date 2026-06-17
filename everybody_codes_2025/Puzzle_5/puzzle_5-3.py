swords = """1:7,1,9,1,6,9,8,3,7,2
2:6,1,9,2,9,8,8,4,3,1
3:7,1,9,1,6,9,8,3,8,3
4:6,1,9,2,8,8,8,4,3,1
5:7,1,9,1,6,9,8,3,7,3
6:6,1,9,2,8,8,8,4,3,5
7:3,7,2,2,7,4,4,6,3,1
8:3,7,2,2,7,4,4,6,3,7
9:3,7,2,2,7,4,1,6,3,7"""

from fishbone import Fishbone

fishbone_swords = []
min = float('inf')
max = 0
for each in swords.split("\n"):
    print(each)
    sword_fishbone = Fishbone(each)
    fishbone_swords.append(sword_fishbone)

values_to_review ={}
for each in fishbone_swords:
    print("####################")
    print(each.print_Fishbone())
    print(each.get_quality())
    print(each.get_level_values())
