# with open("weather_data.csv", mode='r') as weather_file:
#     data = weather_file.readlines();
#     print(data)

import csv
import pandas
from numpy.ma.core import count

# with open("weather_data.csv", mode='r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list_temp = data["temp"].to_list()
# print(data_list_temp)
#
# avg = sum(data_list_temp) / len(data_list_temp)
# print(avg)
#
# avr2 = data["temp"].mean()
# print(avr2)
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data["condition"])
# print(data.condition)
#
# print(data[data.day == 'Monday'])
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == 'Monday']
# fahrenheit = monday.temp * 9/5 + 32
# print(fahrenheit)
#
# data_dictionary = {
#     "students": ['Alla','Olya', 'Kostya'],
#     "scores": [45, 56, 60]
# }
#
# data_csv = pandas.DataFrame(data_dictionary)
# data_csv.to_csv('new_data.csv')

squirrel_dictionary = {
    "Fur coloros": [],
    "Squirrel count": []
}

data_central_park = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241029.csv")
fur_colors = data_central_park['Highlight Fur Color']
data_squirrel = data_central_park['Hectare Squirrel Number']


cinnamon = data_central_park[data_central_park['Highlight Fur Color'] == 'Cinnamon']
print(cinnamon)

count_for_cinnamon = cinnamon['Hectare Squirrel Number'].sum()
squirrel_dictionary['Fur coloros'].append('cinnamon')
squirrel_dictionary['Squirrel count'].append(count_for_cinnamon)

grey = data_central_park[data_central_park['Highlight Fur Color'] == 'Gray']
count_for_grey = grey['Hectare Squirrel Number'].sum()
squirrel_dictionary['Fur coloros'].append('grey')
squirrel_dictionary['Squirrel count'].append(count_for_grey)

white = data_central_park[data_central_park['Highlight Fur Color'] == 'White']
count_for_white = white['Hectare Squirrel Number'].sum()
squirrel_dictionary['Fur coloros'].append('white')
squirrel_dictionary['Squirrel count'].append(count_for_white)

black = data_central_park[data_central_park['Highlight Fur Color'] == 'Black']
count_for_black = black['Hectare Squirrel Number'].sum()
squirrel_dictionary['Fur coloros'].append('black')
squirrel_dictionary['Squirrel count'].append(count_for_black)

print(squirrel_dictionary)

data_squirrel_csv = pandas.DataFrame(squirrel_dictionary)
data_squirrel_csv.to_csv("squirrel count.csv")



double_value = [num *2 for num in range(1,5)]
print(double_value)

names = ['Alex', 'Bath', 'Carolina', 'Dave', 'Elanor', 'Freddie']

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)