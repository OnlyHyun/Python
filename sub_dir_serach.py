import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
       full_filename = os.path.join(dirname, filename)
       ext = os.path.splitext(full_filename)[-1]
       if ext == '.py':
           print(full_filename)

search("C:/Users/Hyun/Python")
print(" ")


def search1(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search1(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search1("C:/Users/Hyun/Python")
