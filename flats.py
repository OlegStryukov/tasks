import random

flats = [[3189226, 1, 11, "построена"], [3500000, 1, 9, "построена"], [3200000, 1, 20, "построена"], [3300000, 1, 8, "построена"], [3400000, 1, 20, "построена"], [3400000, 1, 2, "построена"],[2999000, 2, 16, "построена"], [3490000, 1, 4, "построена"], [2999000, 1, 6, "построена"], [2759730, 1, 1, "строится"], [2369234, 1, 10, "строится"]]

elevator = ['yes','no']

floor = [i for i in range(1,9)]

for i in range(len(flats)):
    flats[i].append(random.choice(elevator))
    flats[i].append(random.choice(floor))
for i, flat in enumerate(flats):
    if not "строится" in flat[3] and flat[2] <= 15 and (flat[4] == 'yes' or flat[5] == 1):
        print (("{0} - {1}").format(i, str(flat)))      