import json
import os

a = "C:\PycharmProjects\HomeWork_WEB\HW_10\hw_django\quotes\json\enemy_losses.json"
# from hw_django.hw_django.settings import BASE_DIR

# json_data = os.path.join(BASE_DIR, 'static', 'json', 'enemy_losses.json')
with open(a, 'r', encoding='utf-8') as fd:
    enemy = json.load(fd)

# data = open(json_data,'r')
print(enemy)
# date_enemy = enemy.pop('date')
# print(date_enemy)
# print('Importing settings from', BASE_DIR)
# print(BASE_DIR)
