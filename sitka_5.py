import csv
from datetime import datetime

in_file1 = open("sitka_weather_2018_simple.csv", "r")
in_file2 = open("death_valley_2018_simple.csv", "r")

csv_file1 = csv.reader(in_file1, delimiter=",")
csv_file2 = csv.reader(in_file2, delimiter=",")

header_row = next(csv_file1)
# print(type(header_row))

# displays index values for each column
for index, column_header in enumerate(header_row):
    print(index, column_header)

# create list for high temps each day
highs1 = []
highs2 = []
# create list for dates
dates1 = []
dates2 = []
# create list for low temps
lows1 = []
lows2 = []

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)

# add high and low temps for Sitka
for temp in csv_file1:
    highs1.append(int(temp[5]))
    lows1.append(int(temp[6]))
    temp_date = datetime.strptime(temp[2], "%Y-%m-%d")
    dates1.append(temp_date)

# add high and low temps for Death Valley
for temp in csv_file2:
    try:
        temp_date = datetime.strptime(temp[2], "%Y-%m-%d")
        high = int(temp[4])
        low = int(temp[5])
    except ValueError:
        print(f"Missing data for {temp_date}")
    else:
        highs2.append(high)
        dates2.append(temp_date)
        lows2.append(low)

# create plot
import matplotlib.pyplot as plt


fig = plt.figure()
"""
plt.plot(dates, highs1, c="red")
plt.plot(dates, lows1, c="blue")

plt.fill_between(dates, highs1, lows1, facecolor="blue", alpha=0.1)

plt.title("Daily High & Low Temps for 2018", fontsize=18)
plt.xlabel("Date of Temp", fontsize=16)
plt.ylabel("Temp. (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

# format date to be at an angle
fig.autofmt_xdate()

plt.show()
"""
# subplots
plt.subplot(4, 1, 1)
plt.plot(dates1, highs1, color="red")
plt.plot(dates1, lows1, color="blue")
plt.fill_between(dates2, highs1, lows1, facecolor="blue", alpha=0.1)
plt.title("Sitka Temps")

plt.subplot(4, 1, 2)
plt.plot(dates2, highs1, color="red")
plt.plot(dates2, lows1, color="blue")
plt.fill_between(dates2, highs1, lows1, facecolor="blue", alpha=0.1)
plt.title("Death Valley Temps")

# format date to be at an angle
fig.autofmt_xdate()

plt.suptitle("Daily High and Low Temps for Sitka and Death Valley 2018", fontsize=18)

plt.show()
