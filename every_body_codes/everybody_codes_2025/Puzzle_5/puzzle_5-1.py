"""
58:5,3,7,8,9,10,4,5,7,8,8
"""
from fishbone import Fishbone
input = "58:5,3,7,8,9,10,4,5,7,8,8"
#input = "95:2,6,7,6,5,8,7,2,7,6,2,5,4,5,2,1,1,8,3,9,1,6,9,4,5,1,4,1,6,9"

fish_bone = Fishbone(input)
fish_bone.print_Fishbone()
print(fish_bone.get_quality())
