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

![Figure 4](https://github.com/agibbs-uscg/IntroToProg-Python-Mod07/blob/master/docs/Figure%204.png "Figure 4.")  

*Figure 4.*  

![Figure 5](https://github.com/agibbs-uscg/IntroToProg-Python-Mod07/blob/master/docs/Figure%205..png "Figure 5.")  

*Figure 5.*  

Figure 6. below shows the script working in cmd.  

![Figure 6](https://github.com/agibbs-uscg/IntroToProg-Python-Mod07/blob/master/docs/Figure%206..png "Figure 6.")  

*Figure 6.*

### Using Exceptions in Python  

Errors detected during execution are called exceptions, according to [Python.org](https://docs.python.org/3/tutorial/errors.html#exceptions). Handling exceptions is a way to use exceptions in a manner decided by the coder. Handling exceptions can be used to return certain detailed errors to users, or it can be used to inform other sections of your code. Using the ‘try’ functions, certain sections of code can be activated, and outcomes can determine outputs. Using a ‘raise’ exception allows the coder to determine the exception beyond those already within python.  

I used exception handling a couple different ways in my code. First, I started with my pickling code from above. One mistake I can foresee a user making that I do not want them to make is entering in a number instead of their name. To ensure this does not happen I created a function called ‘user_errors’. This function takes the user inputs and runs them through a ‘try’ statement. If they are numeric an exception is ‘raised’, ‘else’ the script passing onto the next function. As shown in Figure 7. If the try is completed and a exception is raised, the function prints ‘there was and error!’ and then prints the exception which I set to equal ‘Do not use number for last names’ and the scripts exits. 

```
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
```
*Figure 7.*  

The second way I used exception handling was to fix a possible issue I brought up earlier in this paper. Using the read function by itself within a pickle will only call the first line of file. One way to get all the data back from the file is using exception handling. As shown in Figure 8. I used a ‘while’ loop within my ‘read_data_from_file’ function. This while loop will continue to append objFileData list, reading line by line of the .dat file. As long as the .dat file remains open, the cursor will move from line to line as it is read. If this was done without exception handling, python would not run the script properly and return the error code ‘E0FError’ which is an end of file error because the .dat file will eventually run out of data and thus the last can not be read. To work around this, line 53 for Figure 8. shows that once my code reaches this exception error the while loop ‘breaks’ and the function completes. 
```
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
```
*Figure 8.*  
    
Figure 9. shows my code running in Pycharm if I enter a number for a name. Figure 10 shows my code running in cmd if I enter a number for a name. 
![Figure 9](https://github.com/agibbs-uscg/IntroToProg-Python-Mod07/blob/master/docs/Figure%209..png "Figure 9.")  

*Figure 9.*

![Figure 10](https://github.com/agibbs-uscg/IntroToProg-Python-Mod07/blob/master/docs/Figure%2010%2C.png "Figure 10.")  

*Figure 10.*  

Figure 11. shows my code working in Pycharm and returning the enter data stored in the .dat file.
![Figure 11](https://github.com/agibbs-uscg/IntroToProg-Python-Mod07/blob/master/docs/Figure%2011..png "Figure 11.")

*Figure 11.*

Figure 12. shows my code working in cmd and returning the enter data stored in the .dat file. 
![Figure 12](https://github.com/agibbs-uscg/IntroToProg-Python-Mod07/blob/master/docs/Figure%2012..png "Figure 12.")

*Figure 12.*
## Summary
Through this assignment I the pickle module to write binary code to a recall binary data from .dat file. I also used exception handling to ensure users entered the correct type of data and were shown clear error codes if they did not. I also used exception handling to inform a while loop on when to break. 
