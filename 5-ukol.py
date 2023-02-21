teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# average_temp = [sum(temp)/len(temp) for temp in teploty]
# print("Průměrné teploty pro každý den:" + str(average_temp))

# morning_temp = [temp[0] for temp in teploty]
# print("Ranní teploty:" + str(morning_temp))

# night_temp = [temp[-1] for temp in teploty]
# print("Noční teploty:" + str(night_temp))

# noon_night_temp = [[temp[1], temp[3]] for temp in teploty]
# print("Dopolední a noční teploty:" + str(noon_night_temp))

avg_tmp = []
mor_tmp = []
night_tmp = []
noon_night_tmp = []
for temp in teploty:
    avg_tmp.append(sum(temp)/len(temp))
    mor_tmp.append(temp[0])
    night_tmp.append(temp[-1])
    noon_night_tmp.append([temp[1], temp[3]])
print("Průměrná teplota za každý den: " + str(avg_tmp))
print("Ranní teploty: " + str(mor_tmp))
print("Noční teploty: " + str(night_tmp))
print("Dopolední a noční teploty: " + str(noon_night_tmp))
