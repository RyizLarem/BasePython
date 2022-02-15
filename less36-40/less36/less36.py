''' 
мой день рождения)
00:04PM 10/11/2021
#36.Оператор return в функциях. Функциональное программирование.
'''

def send_mail(from_name):
    text = f"Доброго времени суток {from_name}"
    print(text)


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return (res, x)


def get_max2(a, b):
    return a if a > b else b
 

def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))


PERIMETR = True
if PERIMETR:
    def get_rect(a,b):
        return 2 * (a + b)
else:
    def get_rect2(a, b):
        return a * b


def even(x):
    return x % 2 == 0


for i in range(1, 20):
    if even(i):
        print(i)


print("\n")
print(get_rect(1.5, 3.8))
print("\n")

send_mail("Ryiz\n")
a, b = get_sqrt(49)
print(a, b)
print("________________________\n")
x, y, z = 5, 7, 10
print(get_max2(x, get_max2(y, z)))
a, b, c = 1, 2, 3
# print(get_max3(a, get_max2(b, c)))


