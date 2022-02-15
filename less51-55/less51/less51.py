'''
#51.Функция open. Чтение данных из файла.
'''


file = open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less51/my_file.txt", encoding='utf-8')

# print(file.read(4))
# file.seek(0)
# print(file.read(4))
# pos = file.tell()
# print(pos)

# print(file.readline(), end="") # \n
# print(file.readline(), end=""))


for line in file:
    print(line, end="")


# s = file.readlines()
# print(s)

file.close()


