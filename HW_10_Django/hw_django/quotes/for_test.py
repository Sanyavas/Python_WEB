from hw_django.hw_django.settings import BASE_DIR
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'json', 'enemy_losses.json')
print(file_path)

print(type(BASE_DIR))