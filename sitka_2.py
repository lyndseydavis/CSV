# using datetime module
# adding dates to the x axis for the month of july 2018
import csv
from datetime import datetime

in_file = open("sitka_weather_07-2018_simple.csv", "r")

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

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)

# add high temps to list
for temp in csv_file:
    highs.append(int(temp[5]))
    temp_date = datetime.strptime(temp[2], "%Y-%m-%d")
    dates.append(temp_date)

print(highs)
print(dates)

# create plot
import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")

plt.title("Daily High Temp. - July 2018", fontsize=16)
plt.xlabel("Date of Temp", fontsize=16)
plt.ylabel("Temp. (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()
