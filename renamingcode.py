import os


def rename():
    i = 1
    path = input("Enter folder directory: ")
    new_name = str(input("Rename as what: "))
    for_mat = str(input("Enter the format: "))
    if "\\" in path:
        path = path.replace("\\", "/")
    path += "/"
    for filename in os.listdir(path):
        destination = new_name + " " + str(i) + for_mat
        source = path + filename
        destination = path + destination
        os.rename(source, destination)
        i += 1


rename()
