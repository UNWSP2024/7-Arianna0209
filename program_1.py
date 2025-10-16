# Title: Monthly Rainfall
# Author: Arianna Endres
# Date: 10/15/2025

# This program lets the user enter the total rainfall for each of 12 months into a list.
# The program then calculates and displays the total rainfall for the year,
# the average monthly rainfall, and the months with the highest and lowest amounts.

import statistics

# Input rainfall amount for each month and append to a list.
rainfall_each_month = []
for month in range(12):
    rainfall = float(input(f'How many inches of rainfall did you receive during month {month + 1}? '))
    rainfall_each_month.append(rainfall)

# Calculate and display the total rainfall.
total_rainfall = sum(rainfall_each_month)
print(f'The total rainfall is {total_rainfall} inches')

# Calculate and display the average rainfall
average_rainfall = statistics.mean(rainfall_each_month)
print(f'The average monthly rainfall amount is {average_rainfall} inches')

# Find and display the maximum amount of monthly rainfall.
most_rainfall = (max(rainfall_each_month))
print(f'The most rainfall received in a month was {most_rainfall} inches')

# Find and display the minimum amount of monthly rainfall.
least_rainfall = (min(rainfall_each_month))
print(f'The least rainfall received in a month was {least_rainfall} inches')

