'''
#52.Исключения FileNotFoundError и менджер контекста (with) для файлов.
'''


try:
    # file = open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less52/mf.txt", encoding="utf-8")
    with open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less52/mf.txt", encoding="utf-8") as file:
        s = file.readlines()
        print(s)
    print(file.closed)
    # try:
    #     s = file.readlines()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")
    print(file.closed)


