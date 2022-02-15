'''
#55.Функция-генератор. Операторы yield.
'''


# def get_list():
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a) / len(a)


# a = get_list()
# print(list(a))


def find_word(f, word):
    g_index = 0
    for line in f:
        index = 0
        while(index != -1):
            index = line.find(word, index)
            if index > -1:
                yield g_index + index
                index += 1

        g_index += len(line)



try:
    with open("SelfEducation/BasePython3/less51-55/less55/lesson55.txt", encoding="utf-8") as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Ошибка обработки файла")




