''' 
AM 11/11/2021
#44.Замыкания в Python
'''


# def say_name(name):
#     def say_goodbye():
#         print("Don't say me goodbye, " + name + "!")

#     return say_goodbye


# f = say_name("Danil")
# f2 = say_name("Python")
# f()
# f2()


# счётчик запусков
# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
    
#     return step


# c1 = counter(10)
# c2 = counter()
# print(c1(), c2())
# print(c1(), c2()) 
# print(c1(), c2()) 


#


def stip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = stip_string()
strip2 = stip_string(" !?,.;")

print(strip1(" hello python!.. "))
print(strip2(" hello python!.. "))