# address-register
## This project is a system designed to insert new addresses and listing the existing ones.

First of all, i would like to make some observations about this project:
- I was supposed to use the framework Django and API's in order to develop this project, but since i don't have many experiences in using them, i decided to stick
with what i already know, which is, the Python language itself;

- I also was supposed to use some database in order to register the addresses in the system, but since i also don't have many experiences yet in databases, i decided
to register the elements in a CSV file, which will be working as the database of the system;

 The project consists in 4 (four) files:
- main_screen.py
- classes_and_functions.py
- reset_screen.py
- addresses.csv

 **main_screen.py** file is the file that has to be executed, because it is the one responsible for the whole execution of the system, as well the loop to keep it working
as intended.  
 **classes_and_functions.py** file is the one that contains all the classes and functions that interact with our system, in order to make it work as clean as possible.  
 **reset_screen.py** is a file that contain some functions that clean up the terminal/console screen, to make sure that the user doesn't get frustrated with tons of 
 information in the screen.  
  **addresses.csv** is the file that will be used as database for this project. In case that file doesn't exists for some reason, the system auto generates a new one.  
