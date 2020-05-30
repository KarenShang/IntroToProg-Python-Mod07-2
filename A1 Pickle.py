# ------------------------------------------------- #
# Title: Assignment07_Pickling
# Description: A simple example of storing data in a binary file through pickling
# ChangeLog: (Who, When, What)
# AGibbs, 30May2020, created pickling demo code
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# varibles -------------------------------------------- #
strFileName = 'AppData.dat'
list_of_data = [] #created from user input
strFist = None #string input data
strLast = None #string input data


# Processing -------------------------------------- #
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
    objfile = open(file_name, 'rb')
    objFileData = pickle.load(objfile)
    objfile.close()
    return objFileData


# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
strFirst = input('Please input your first name: ')
strLast = input('Please input your last name: ')
list_of_data = [strFirst, strLast]
# TODO: store the list object into a binary file
save_data_to_file(strFileName, list_of_data)
# TODO: Read the data from the file into a new list object and display the contents
print(read_data_from_file(file_name=strFileName))




