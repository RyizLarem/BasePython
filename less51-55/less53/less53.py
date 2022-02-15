'''
#53.Запись данных в файл в текстовом и бинарном режимах.
'''

import pickle

# Вариант №1
# file = open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out.txt","w")
# for i in range(1000, 0, -7):    
    
#     file.write(f"{i}\n")

# file.write("\tI'm GHOUL")
# file.close()

# # Вариант №2
# file = open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out.txt","w")
# [file.write(f"{i}\n") for i in range(1000, 0, -7)]
# file.write("\tI'm GHOUL")
# file.close()

# try:
#     with open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out.txt","w") as file:
#         for i in range(1000, 0, -7):
#             file.write(f"{i}\n")
#         file.write("\n\tI'm GHOUL")
    
# except FileNotFoundError:
#     print("Файл не удалось открыть")    
# except:
#     print("Ошибка при работе с файлом")
# finally:
#     print(file.closed)



# try:
#     with open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out.txt","a+") as file:
#         file.seek(0)
#         file.writelines(["hello12345\n", "\nsdfsw"])
#         s = file.readlines()
#         print(s)
# except FileNotFoundError:
#     print("Файл не удалось открыть")    

# except:
#     print("Ошибка при работе с файлом")


#
#
#


# books = [        b1 = pickle.load(file)
, 250),
#     ("Мастер и Маргарита", "Булгаков М.А.", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# ]


# file = open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out2.bin", "wb")
# pickle.dump(books, file)
# file.close()


# file = open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out2.bin", "rb")
# bs = pickle.load(file)
# file.close()
# print(bs)

#
#


books1 = ["Евгений Онегин", "Пушкин А.С.", 200]
books2 = ["Муму", "Тургенев И.С.", 250],
books3 = ["Мастер и Маргарита", "Булгаков М.А.", 500],
books4 = ["Мертвые души", "Гоголь Н.В.", 190]

# записывать в бинарном режиме
try:
    with open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out2.bin", "wb") as file:
        pickle.dump(books1, file)
        pickle.dump(books2, file)
        pickle.dump(books3, file)
        pickle.dump(books4, file)
except:
    print("Ошибка при работе с файлом")


# считывать в бинарном
try:
    with open("/home/ryiz/Документы/MyProjectPython/SelfEducation/BasePython3/less51-55/less53/out2.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except:
    print("Ошибка при работе с файлом")

print(b1, b2, b3 ,b4, sep="\n")