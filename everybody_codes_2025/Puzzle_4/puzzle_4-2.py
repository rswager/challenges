"""

"""
def calculate_rotation_factor(gears: list[int]):
    rotation_factor = 1
    for i in range(len(gears) - 1):
        rotation_factor= rotation_factor*(gears[i] / gears[i + 1])

    return rotation_factor

min = 10_000_000_000_000
gears = [128,64,32,16,8]
print(int(min/calculate_rotation_factor(gears)))

gears = [102,75,50,35,13]
print(int(min/calculate_rotation_factor(gears))+1)

gears = """985
981
970
968
945
928
922
896
887
862
841
825
813
802
787
773
753
730
706
679
654
630
602
596
575
549
538
511
499
491
476
460
442
418
415
413
407
388
371
362
339
311
310
300
284
269
248
233
231
204"""
gears = [int(x) for x in gears.split("\n")]
print(int(min/calculate_rotation_factor(gears))+1)
