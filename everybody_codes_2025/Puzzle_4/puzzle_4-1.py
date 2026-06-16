"""
[128,64,32,16,8]
"""

def calculate_rotation_factor(gears: list[int]):
    rotation_factor = 1
    for i in range(len(gears) - 1):
        rotation_factor= rotation_factor*(gears[i] / gears[i + 1])

    return rotation_factor


gears = [128,64,32,16,8]
rotation_factor = calculate_rotation_factor(gears)
print(int(rotation_factor*2025))

gears = [102,75,50,35,13]
rotation_factor = calculate_rotation_factor(gears)
print(int(rotation_factor*2025))

gears = """1000
977
966
963
943
921
900
879
872
848
841
833
817
807
799
789
781
753
725
713
685
656
627
600
584
583
557
537
528
523
506
480
469
448
433
419
390
367
354
350
338
330
324
311
306
280
254
235
207
196"""
gears = [int(each) for each in gears.split("\n")]
print(int(calculate_rotation_factor(gears)*2025))