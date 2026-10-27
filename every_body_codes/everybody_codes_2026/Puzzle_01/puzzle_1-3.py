from math import sqrt,floor
from typing import List

def return_fortification_size(remaining_pinecones: int) -> int:
    """
    To calculate the fortification size we will:
     - floor the square root of the remaining_pinecones
     - If that integer is even we add 1 to make it odd
     - If that integer is odd we add 2 to make it odd
        - We don't stay at this odd number becasue we are (nxn) in size but that only needs (nxn)-1
            so we need to go up to the next odd integer
    - If the integer is less than 3 we return 3

    :param remaining_pinecones: number of pinecones the fortification i
    :return: always a postive integer that is odd and greater than 2
    """
    size = floor(sqrt(remaining_pinecones))
    if size % 2 == 0:
        size += 1
    else:
        size += 2
    return size if size >= 3 else 3

def return_required_pinecones(size: int) -> int:
    """Just missing the middle, so (size*size)-1"""
    return (size*size)-1

if __name__ == "__main__":
    fortifications: List[int]  = [3,11,12,16,24,25]
    pinecones_needed = 0
    for fort_pinecones in fortifications:
        fortification_size = return_fortification_size(fort_pinecones)
        pinecones_needed += return_required_pinecones(fortification_size) - fort_pinecones
    print(pinecones_needed)
