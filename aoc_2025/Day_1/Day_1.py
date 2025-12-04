def crack_the_code(start_pos, rotation_list_in, target_number=0,dial_size=100):
    target_reached = 0
    current_position = start_pos
    for each in rotation_list_in:
        direction = 1 if each[0] == 'R' else -1
        step = direction * int(each[-(len(each)-1):])
        current_position = (current_position+step)% dial_size
        target_reached += 1 if current_position == target_number else 0
    return target_reached

def crack_the_code_0x434C49434B_method(start_pos, rotation_list_in, target_number=0,dial_size=100):
    target_passed = 0
    current_position = start_pos
    for each in rotation_list_in:
        direction = 1 if each[0] == 'R' else -1
        step = int(each[-(len(each)-1):])
        # If we made some complete rotations let's calculate those
        if step >= dial_size:
            # number of complete rotations (how many times we passed 0)
            target_passed += int(step/dial_size)
            # remove those steps and then process remaining
            step -= (int(step/dial_size)*dial_size)

        if step > 0:
            next_position = (current_position+(direction*step))% dial_size
            target_passed += 1 if (((direction == 1 and next_position < current_position) or
                                   (direction == -1 and next_position > current_position)) or
                                   next_position == target_number) else 0


        current_position = next_position
    return target_passed


if __name__ == "__main__":
    # """ Part one of the code """
    start = 50
    #rotations = ['L100','L1']
    rotations = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    #print(len(rotations))
    print(crack_the_code(start_pos=start,rotation_list_in=rotations))


    """0x434C49434B Method"""
    print(crack_the_code_0x434C49434B_method(start_pos=start,rotation_list_in=rotations))
