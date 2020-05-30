# Use of Python Exceptions and Pickling
**Adam Gibbs**  
**30 May 2020**
## Introduction
This page will discuss how to use .dat file within Python script and how to use python exception handling to relay errors to users. I will use Pycham to create two sets of scripts, first is will use picking to convert data into a .dat and then covert the data within that file back to a readable form.  Second, using the same script, I will use exception functions to relay errors to the user and to stop a read function within the script. 


## How the script works
Using the Python script editing tool PyCharm, I started my script by importing the pickle module and declaring variables that I used throughout the script. Figure 1. Shows the variables I defined. 
```
import pickle  # This imports code from another code file!
# varibles -------------------------------------------- #
strFileName = 'AppData.dat'
list_of_data = [] #created from user input
strFist = None #string input data
strLast = None #string input data
```
*Figure 1.*  
The next step in my script was to define functions that will be used later in my script. 

### Creating and processing .dat files with Pickle
Per [Python.org](https://docs.python.org/3/library/pickle.html), ‘The pickle module implements binary protocols for serializing and de-serializing a Python object structure’. This can be especially useful when trying to decrease the size and storage space needed for your script and working files. For this script I defined two functions, one to write the binary code to a .dat file and the second to read the data from the binary coded .dat file, see Figure 2.  
```
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
```
*Figure 2.*  
Figure 2., starts function ‘save_data_to_file’ with parameter ‘file_name’ and ‘list_of_data’. This function opens a .dat file and readies it to be appended ('ab' in line 23). ‘ab’ is used to append binary code. ‘pickle.dump()’ on line 24 tell the script to dump to write the data within ‘list_of_data’ as binary code into the open file. Final the function closes the file. 
The next function in Figure 2., starts the function read_data_from_file’ with parameter ‘filename’. This function opens the .dat file and prepares it to be read (‘rb’ in line 22). The binary code is then converted back and loaded in mem as ‘objFileData’ using ‘pickle.load()’. The file is closed, and the function returns the variable objFileData to be used.  

With the functions set, my code then goes to presentation section shown in Figure 3. 
```
 Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
strFirst = input('Please input your first name: ')
strLast = input('Please input your last name: ')
list_of_data = [strFirst, strLast]
# TODO: store the list object into a binary file
save_data_to_file(strFileName, list_of_data)
# TODO: Read the data from the file into a new list object and display the contents
print(read_data_from_file(file_name=strFileName))
```
*Figure 3.*  
My script asks for input from the user which sets variables ‘strFirst’ and ‘strLast’ in lines 41 and 42 of Figure 3. These two variables are then used to create variable ‘list_of_data’ on line 43. I then call function ‘save_data_to_file’ and then I call function ‘read_data_from_file’ and print its result. As constructed, this will only read and return the first line with the .dat file. This will be address in the next section of this paper. 
Figure 4. below shows the script working in Pycharm and Figure 5. Shows the created .dat file. Note that the data is more or less unreadable in the .dat file as it has been converted through pickling.



### Using Exceptions in Python
## Summary
Through this assignment I the pickle module to write binary code to a recall binary data from .dat file. I also used exception handling to ensure users entered the correct type of data and were shown clear error codes if they did not. I also used exception handling to inform a while loop on when to break. 
