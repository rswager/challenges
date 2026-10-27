from math import sqrt
from typing import List

def return_fortification_size(remaining_pinecones: int) -> int:
    """
    We can fine the size of our fortification by taking the sqare root of our remaining pinecones.
    If we have a float we will chop off the decimal and add 1 to get us our next size fortification, as
        we currently have more than enough for the current size.
    If we have an integer we have exactly enough for the current size fortification.

    :param remaining_pinecones: number of pinecones the fortification has
    :return:
    """
    pinecones_radius: float = sqrt(remaining_pinecones)
    if pinecones_radius%1 == 0:
        return int(pinecones_radius)
    else:
        return int(pinecones_radius)+1

def return_required_pinecones(size: int) -> int:
    """since the fortification is nxn we can just return size*size"""
    return size*size

if __name__ == "__main__":
    fortifications: List[int] = [3,11,12,16,24,25]
    pinecones_needed = 0
    for fort_pinecones in fortifications:
        fortification_size = return_fortification_size(fort_pinecones)
        required: int = return_required_pinecones(fortification_size)
        pinecones_needed += required-fort_pinecones

    print(pinecones_needed)
