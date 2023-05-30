from hw_django.hw_django.settings import BASE_DIR
import os
import pathlib

p = pathlib.Path(__file__)
print(p)

b = 5
a = 6

c = a.__add__(b)

print(c)