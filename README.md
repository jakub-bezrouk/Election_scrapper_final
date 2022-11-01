Engeto: Project 3
The third project at the online python academy by Engeto.

Description of assignment
This project is used to extract the results of the parliamentary elections in 2017.

Installing libraries
The libraries that are used in the code are stored in the requirements.txt file.

$ pip3 --version # pip version
$ pip3 install -r requirements.txt # install libraries
Starting a project Running the .election-scraper.py. 


Sample project
Voting results for district Brno-venkov:

argument: (https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203) argument: brno_venkov.csv 

Download progress:

Vše je v pořádku, stahuji data.
Stahuji 1 z 116   Adamov
Stahuji 2 z 116   Bedřichov
Stahuji 3 z 116   Benešov
...
Data stáhnuty ve složce programu.


Program description
At the beginning of the program it is necessary to import the libraries that we will work with in the program.

line 6 - line 7 - Assigning URL and name of CSV. 

line 12 - line 25 - Program check the URL and name of CSV. If the user has entered the wrong URL or user use forbiden characters in name of CSV, then the program notifies him and ends program. 
wrong message: Zkontroluj správnost odkazu či jména CSV. Nesmí být zakázané znaky!) (~ # % & * : < > ? / \ { | }.)

line 29 - line 47 - At first, program get all middle links from user URL, cities and codes. After that, program open first middle link and save parties for first row in csv

line 50 - line 69 - Program downloads data from each middle link about votes, envelopes, registered, etc via function named "data". Editing them and save them to list named "Done" via fuction named "up_to_1k". 

line 73 - line 82 -  Program make CSV named after user choice + "_vysledky_2017.csv" and write in the first row names from "fw" = (Kód, město, ..) and names of parties from "parties". Function named "write_to_csv" writes data from "Done" and clear "Done" after it. 

line 84 - line 88 - Function named "final" opens directory of program and maked CSV file.

line 92 - line 103 - Loop, which opens middle link after middle link. At first, number of code city and name city will be saved to "Done". Loop start fuction named "data", which download data from midle link (line 50-69) and start fuction named "write_to_csv". 

line 103 - When loop ends, program start fuction named "final". Which opens directory of program with maked CSV.
