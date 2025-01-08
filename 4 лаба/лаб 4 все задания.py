#Задание 1
import math
chislo_input = int(input('Введите число: '))
print(math.sqrt(chislo_input))

#Задание 2
import datetime
c_t = datetime.datetime.now()
print(c_t)

#Задание 3
import my_module as mm
result = mm.add(7,1)
print(result)

#Задание 4
from package.module1 import say_py
say_py()
from package.module2 import square
square(4)