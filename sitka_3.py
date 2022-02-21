# change file to include all 2018 data
# change title to include daily low and high temps
# extract low temps from file and add to chart
# shade area between high and low temps


import csv
from datetime import datetime

in_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(in_file, delimiter=",")

header_row = next(csv_file)
# print(type(header_row))

# displays index values for each column
# for index, column_header in enumerate(header_row):
# print(index, column_header)

# create list for high temps each day
highs = []
# create list for dates
dates = []
# create list for low temps
lows = []

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)

# add high temps to list
for temp in csv_file:
    highs.append(int(temp[5]))
    temp_date = datetime.strptime(temp[2], "%Y-%m-%d")
    dates.append(temp_date)
    lows.append(int(temp[6]))

print(highs)
print(dates)
print(lows)

# create plot
import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily High & Low Temps for 2018", fontsize=18)
plt.xlabel("Date of Temp", fontsize=16)
plt.ylabel("Temp. (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

# format date to be at an angle
fig.autofmt_xdate()

plt.show()

# subplots
plt.subplot(2, 1, 1)
plt.plot(dates, highs, color="red")
plt.title("High Temps")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, color="blue")
plt.title("Low Temps")

plt.suptitle("Daily High and Low Temps for 2018 - Sitka, AK", fontsize=18)

plt.show()
