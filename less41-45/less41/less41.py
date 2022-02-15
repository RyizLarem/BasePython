''' 
5:42AM 11/11/2021
#41.Рекурсивные функции.
'''

# def recursive(value):
#     print(value)
#     if value < 4:
#         recursive(value+1)
#     print(value)


# recursive(1)


# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n-1)
    

# p = fact(6)
# print(p)


F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'zipfldr.dll']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(" "*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print(" "*(depth+1), " ".join(path[f]))


get_files(F)

