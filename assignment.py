import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_sitka = open("sitka_weather_2018_simple.csv", "r")
open_dv = open("death_valley_2018_simple.csv", "r")

sitka = csv.reader(open_sitka, delimiter=",")
dv = csv.reader(open_dv, delimiter=",")

header_row1 = next(sitka)
header_row2 = next(dv)
# print(type(header_row))

# create index variables
tmin1 = header_row1.index("TMIN")
tmax1 = header_row1.index("TMAX")
tmin2 = header_row2.index("TMIN")
tmax2 = header_row2.index("TMAX")
title1 = header_row1.index("NAME")
title2 = header_row2.index("NAME")

# create lists for highs, lows, and dates
highs1, highs2, dates1, dates2, lows1, lows2 = [], [], [], [], [], []

# add high and low temps for Sitka
for temp in sitka:
    try:
        date = datetime.strptime(temp[2], "%Y-%m-%d")
        high = int(temp[tmax1])
        low = int(temp[tmin1])
        sitka_title = temp[title1]
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs1.append(high)
        dates1.append(date)
        lows1.append(low)

# add high and low temps for Death Valley
for temp in dv:
    try:
        date = datetime.strptime(temp[2], "%Y-%m-%d")
        high = int(temp[tmax2])
        low = int(temp[tmin2])
        dv_title = temp[title2]
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs2.append(high)
        dates2.append(date)
        lows2.append(low)

# create plot
fig = plt.figure()

# subplots
plt.subplot(2, 1, 1)
plt.plot(dates1, highs1, color="red")
plt.plot(dates1, lows1, color="blue")
plt.fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)
plt.title(sitka_title)

plt.subplot(2, 1, 2)
plt.plot(dates2, highs2, color="red")
plt.plot(dates2, lows2, color="blue")
plt.fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
plt.title(dv_title)

# format date to be at an angle
fig.autofmt_xdate()

plt.suptitle(
    f"Temperature comparison between {sitka_title} and {dv_title}", fontsize=18
)

plt.show()
