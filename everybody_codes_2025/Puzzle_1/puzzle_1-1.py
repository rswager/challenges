"""
Oryaris,Rylarvash,Orahzyth,Maralendris,Gavtal,Raltal,Vyrzar,Vornrex,Drakdra,Tharkyris

L1,R5,L7,R3,L2,R6,L2,R8,L6,R6,L3
"""
names = "Oryaris,Rylarvash,Orahzyth,Maralendris,Gavtal,Raltal,Vyrzar,Vornrex,Drakdra,Tharkyris"
instuctions = "L1,R5,L7,R3,L2,R6,L2,R8,L6,R6,L3"
list_of_names = names.split(",")
list_of_instuctions = instuctions.split(",")
print(list_of_names)
print(list_of_instuctions)

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

current_index = 0
max_index = len(list_of_names)-1
min_index = 0

for instruction in list_of_instuctions:
    direction, lenth = -1 if instruction[0] == "L" else 1, int(instruction[1:])
    current_index += (direction * lenth)
    current_index = clamp(current_index, min_index, max_index)

print(list_of_names[current_index])
