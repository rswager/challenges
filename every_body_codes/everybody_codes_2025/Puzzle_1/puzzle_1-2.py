"""
Havcalyx,Ilmaraes,Fyndvalir,Haroryx,Grimmal,Mornophis,Mornynn,Nyrixaxar,Azmarnoris,Larmal,Talaes,Krynntal,Oryilor,Garfelix,Qyraelor,Yndxel,Brivfeth,Lornfelix,Kronthyn,Aureadarin

L10,R10,L7,R12,L12,R18,L15,R14,L13,R18,L5,R13,L5,R18,L5,R10,L5,R18,L5,R18,L10,R10,L13,R17,L13,R11,L14,R7,L5
"""

names = "Havcalyx,Ilmaraes,Fyndvalir,Haroryx,Grimmal,Mornophis,Mornynn,Nyrixaxar,Azmarnoris,Larmal,Talaes,Krynntal,Oryilor,Garfelix,Qyraelor,Yndxel,Brivfeth,Lornfelix,Kronthyn,Aureadarin"
list_of_names = names.split(",")
instuctions = "L10,R10,L7,R12,L12,R18,L15,R14,L13,R18,L5,R13,L5,R18,L5,R10,L5,R18,L5,R18,L10,R10,L13,R17,L13,R11,L14,R7,L5"
list_of_instuctions = instuctions.split(",")

current_index = 0
max_index = len(list_of_names)
min_index = 0
for instruction in list_of_instuctions:
    print(current_index,list_of_names[current_index])
    direction, lenth = -1 if instruction[0] == "L" else 1, int(instruction[1:])
    current_index = (current_index + (direction * lenth)) % max_index



print(list_of_names[current_index])