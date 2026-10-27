from math import sqrt, ceil
from typing import List

def return_fortification_size(remaining_pinecones: int) -> int:
    """
    4(n-1) is our requried pinecones for the fortification. If we set that equal to our remaining pinecones
    then solve for n we can see if we get an integer.

    4(n-1) = remaining_pinecones -> n-1 = (remaining_pinecones/4)
    n = (remaining_pinecones/4)+1

    This will not give us an integer. Since we are alwasy looking for the next biggest fortification we can
        ceil the value to get our fortification size

    Finally, we need to ensure a size of 3 is the smallest. So we return 3 if that is the case.

    :param remaining_pinecones: number of pinecones the fortification has
    :return: always a postive integer that is odd and greater than 2
    """
    size: int = ceil((remaining_pinecones/4)+1)
    size = size if size >= 3 else 3
    return size


def return_required_pinecones(size: int) -> int:
    """
        Since the fortification is a sqare (nxn) in size. We can add up two sets of sides to calulate the size.
            - side 1 and 2 are n and n -> 2n
            - side 3 and 4 are (n-2) and (n-2) -> 2(n-2)
        So 2n + 2(n-2) -> 2n + 2n - 4 -> 4n -4  -> 4(n - 1)
        4(n-1) is our requried pinecones for the fortification
    :param size: the dimension of our fortification in integers
    :return:
    """
    return 4*(size-1)

if __name__ == '__main__':
    fortifications: List[int] = [3,11,12,16,24,25]
    pinecones_needed = 0
    for fort_pinecones in fortifications:
        fortification_size = return_fortification_size(fort_pinecones)
        pinecones_needed += return_required_pinecones(fortification_size)-fort_pinecones
    print(pinecones_needed)