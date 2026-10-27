from sqlalchemy import false


def crack_the_code(start_pos, rotation_list_in, target_number=0,dial_size=100):
    target_reached = 0
    current_position = start_pos
    for each in rotation_list_in:
        direction = 1 if each[0] == 'R' else -1
        step = int(each[1:])
        current_position = (current_position+(direction*step))% dial_size
        target_reached += 1 if current_position == target_number else 0
    return target_reached

def crack_the_code_0x434C49434B_method(start_pos, rotation_list_in, target_number=0, dial_size=100):
    target_passed = 0
    current_position = start_pos

    for each in rotation_list_in:
        direction = 1 if each[0] == 'R' else -1
        step = int(each[1:])

        # Count full rotations
        target_passed += step // dial_size

        # Remaining partial movement
        step = step % dial_size
        if step > 0:
            # Calcualte Next Position
            next_position = (current_position + direction * step) % dial_size

            passed = False

            if direction == 1:  # moving right
                if current_position  < next_position :
                    passed = (current_position < target_number <= next_position)
                else:  # wrap
                    passed = ( target_number > current_position or target_number <= next_position )

            else:  # direction == -1, moving left
                if next_position < current_position:
                    passed = (next_position <= target_number < current_position)
                else:  # wrap
                    passed = (target_number < current_position or target_number >= next_position)

            if passed:
                target_passed += 1

            current_position = next_position

    return target_passed



def crack_the_code_0x434C49434B_method_simple(start_pos, rotation_list_in, target_number=0, dial_size=100):
    target_passed = 0
    current_position = start_pos
    for each in rotation_list_in:
        direction = 1 if each[0] == 'R' else -1
        step = int(each[1:])
        for _ in range(step):
            current_position = (current_position+direction)% dial_size
            target_passed += 1 if (current_position == target_number) else 0

    return target_passed

if __name__ == "__main__":
    # """ Part one of the code """
    start = 50
    #rotations = ['L100','L1']
    rotations = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    print(crack_the_code(start_pos=start,rotation_list_in=rotations))


    """0x434C49434B Method"""
    print(crack_the_code_0x434C49434B_method(start_pos=start,rotation_list_in=rotations))
    print(crack_the_code_0x434C49434B_method_simple(start_pos=start,rotation_list_in=rotations))