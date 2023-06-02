import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
enemy_loses_json = os.path.join(current_dir, 'json', 'enemy_losses.json')


with open(enemy_loses_json, 'r', encoding='utf-8') as fd:
    enemy = json.load(fd)
date_enemy = enemy[0].pop('date')

print(enemy)
print("++++++")
print(date_enemy)
