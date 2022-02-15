''' 
AM 11/11/2021
#43.Области видимости переменных. Ключевые слова global и nonlocal
'''


# N = 100
# WIDTH, HEIGHT = 1000, 500


# def my_func(lst):
#     global N
#     N = 20
#     for x in lst:
#         n = x + 1 + N
#         print(n)


# my_func([1, 2, 3])
# print(N)


# x = 0


# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print("inner: ", x)
    
#     inner()
#     print("outer: ", x)

# outer()
# print("global: ", x)




x = 0


def outer():
    x = 1
    def inner():
        nonlocal x
        x = 20
        print("inner: ", x)
    
    inner()
    print("outer: ", x)

outer()
print("global: ", x)



