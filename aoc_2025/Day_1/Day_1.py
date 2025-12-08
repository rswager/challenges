def crack_the_code(start_pos, rotation_list_in, target_number=0,dial_size=100):
    target_reached = 0
    current_position = start_pos
    for each in rotation_list_in:
        direction = 1 if each[0] == 'R' else -1
        step = direction * int(each[-(len(each)-1):])
        current_position = (current_position+step)% dial_size
        target_reached += 1 if current_position == target_number else 0
    return target_reached

def crack_the_code

if __name__ == "__main__":
    start = 50
    rotations = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    print(crack_the_code(start_pos=start,rotation_list_in=rotations))
