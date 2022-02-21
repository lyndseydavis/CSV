import csv

in_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(in_file, delimiter=",")

header_row = next(csv_file)
# print(type(header_row))

# displays index values for each column
# for index, column_header in enumerate(header_row):
# print(index, column_header)

# create list for high temps each day
highs = []

for temp in csv_file:
    highs.append(int(temp[5]))

print(highs)

# create plot
import matplotlib.pyplot as plt

plt.plot(highs, c="red")

plt.title("Daily High Temp. - July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temp. (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
