#Задание 1
def greet(name):
    return f'Hello, {name}!'
print(greet('Макар'))

#Задание 2
x = int(input('введите число: '))
def square(x):
    return x**2
print(square(x))

#Задание 3
def max_of_two(n,m):
    if n>m:
        return n
    else:
        return m
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
x=max_of_two(a,b)
print(x)


# Задание 4
def describe_person(name, age = 30):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
describe_person('Макар')


#Задание 5
def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True
print(is_prime(int(input('Введите число: '))))