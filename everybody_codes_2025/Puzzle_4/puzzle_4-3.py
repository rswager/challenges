"""
Blah
"""
def calculate_rotation_factor(gears: list[list[int]]):
    rotation_factor = 1
    for i in range(len(gears) - 1):
        print(gears[i], gears[i + 1], rotation_factor)
        # Start Case
        if i == 0:
            # The first gear ratio to the Left Gear of 2nd
            rotation_factor = rotation_factor * (gears[i][0]/gears[i+1][0])

        # Mid Case
        if i > 0 and i< len(gears) - 1:
            rotation_factor = rotation_factor * (gears[i][1]/gears[i+1][0])

        # End Case
        if i == len(gears) - 1:
            rotation_factor = rotation_factor * (gears[i][1]/gears[i+1][0])
    return (rotation_factor)


def resolve_gear(raw_gears: str):
    gears = []
    for each in raw_gears.split("\n"):
        if "|" in each:
            gears.append([int(x) for x in each.split("|")])
        else:
            gears.append([int(each)])
    return gears

raw_gears = """5
5|10
10|20
5"""
gears = resolve_gear(raw_gears)

print(int(calculate_rotation_factor(gears)*100))

raw_gears = """5
7|21
18|36
27|27
10|50
10|50
11"""
gears = resolve_gear(raw_gears)
print(int(calculate_rotation_factor(gears)*100))

raw_gears = """682
672|672
654|2616
647|647
644|644
636|636
618|618
609|609
594|1188
589|589
587|1761
574|574
570|2280
555|555
548|2192
547|547
538|1076
525|525
515|1030
496|496
495|1980
491|491
483|1932
466|466
465|930
460|460
453|453
439|439
425|425
411|411
410|1640
407|407
392|1568
385|385
384|1536
377|377
366|732
351|351
349|1396
333|333
316|316
298|298
285|855
281|281
262|786
246|246
242|484
232|232
213|213
182"""
gears = resolve_gear(raw_gears)
print(int(calculate_rotation_factor(gears)*100))