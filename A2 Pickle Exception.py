# ------------------------------------------------- #
# Title: Assignment07_Pickling
# Description: A simple example of storing data in a binary file through pickling
# ChangeLog: (Who, When, What)
# AGibbs, 30May2020, copied pickling demo code, added exceptions
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# varibles -------------------------------------------- #
strFileName = 'AppData.dat'
list_of_data = [] #created from user input
strFist = None #string input data
strLast = None #string input data


# Processing -------------------------------------- #
def user_errors(strFirst, strLast):
    try:
        if strFirst.isnumeric():
            raise Exception ('Do not use numbers for first names')
        elif strLast.isnumeric():
            raise Exception ('Do not use numbers for last names')
        else:
            pass

    except Exception as e:
        print("There was an error!")
        print(e)
        exit()

def save_data_to_file(file_name, list_of_data):
    """ Saves data to .dat file
        :param file_name: (string) with name of file:
        :param list_of_data: (list) you want filled with file data:
     """
    objFile = open(file_name, 'ab')

    pickle.dump(list_of_data, objFile)
    objFile.close()


def read_data_from_file(file_name):
    """ reads data to .dat file
       :param file_name: (string) with name of file:

    """
    objFileData = []
    objfile = open(file_name, 'rb')
    while True:
        try:
            objFileData.append(pickle.load(objfile))
        except EOFError:
            break
    objfile.close()
    return objFileData


# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
strFirst = input('Please input your first name: ')
strLast = input('Please input your last name: ')
user_errors(strFirst, strLast)
list_of_data = [strFirst, strLast]



# TODO: store the list object into a binary file
save_data_to_file(strFileName, list_of_data)


# TODO: Read the data from the file into a new list object and display the contents
lstData = (read_data_from_file(file_name=strFileName))
for row in lstData:
    print(row)


