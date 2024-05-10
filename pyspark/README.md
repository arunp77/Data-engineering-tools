# Tasks and descriptions for each case

## Task-1 : Directory Listing
Write a function that takes the name of a directory (string) and prints out the path of the files within that directory as well as any files contained in its sub directories. This function is similar to ‘os.walk’. Please do not use ‘os.walk’ in your answer. We are interested in your ability to work with nested structures.

### Description
In this case, created a `directory.py` file. Here first imported the `os` module and later created the `list_files(directory)` function which will print the path of each file in a directory and its subdirectories. Here, I'm using the `os.walk()` function to traverse through the directory structure starting from the specified `directory`. Within each iteration of the traversal, I'm retrieving the root directory, a list of subdirectories (`dirs`), and a list of files (`files`). Then, for each file found, I'm constructing its full file path using `os.path.join()` and printing it out. Essentially, this code allows me to list all the files within the specified directory and its subdirectories.


## Task-2 : Latitude and Longitude
Create a ‘coordinate_combiner' function that receives two input lists (latitudes and longitudes) and combines them as a single list of tuples. If the lists have different sizes, the output should have the same size as the shortest list. In addition, the required ‘coordinate_combiner’ function should replace negative (and zero) longitudes by the keyword ‘WEST’. Implement the 'coordinate_combiner’ function and supply it with unit tests covering the given cases (Case 1,2,3 and 4). It should be possible to execute 'pytest' directly on the directory where the application is stored to execute the tests.


### Description
The Coordinate Combiner is a Python function that combines latitude and longitude coordinates into tuples, replacing negative and zero longitudes with the keyword 'WEST'. Have created two files:
- `cordinate_combine.py` : main function that combines the coordinates 
- `test_cordinate_combine.py` : For the pytest purpose. Here first imported the function which combines the coordinates (`coordinate_combiner(latitudes, longitudes)`) from the `cordinate_combine.py` and defined 4 use case functions to combine the coordinates.
- To test, just run the test script 
  ```bash
  pytest -s test_coordinate_combiner.py
  ``` 
  The output will also print the test cases
  (Here -s is placed to allows print statements within the test functions to be displayed in terminal).

  ![alt text](pytest.png)


## Task-3 :	Read and parse a log message
The following log message is indicating when a Sentinel-3 file has been received in the archive:

![alt text](archive.png)

The log message would look in the archive.log file as follows:
```
22.262.10.37.41.882	UMARF	oumafis302	LogFileAgent	I	proftpd_xferlog: Mon Sep 19 10:37:33 2022 0 10.13.6.63 9799680 /ingestion/umarf/NOM/sfe/input/S3A_SR_2_WAT____20220919T083843_20220919T084434_20220919T103642_0351_090_078______MAR_O_NR_005.SEN3.tar.tmp b _ i r s3user ftp 0 * c
```

In yellow highlighted the file size and the filename of the Sentinel-3 product received. 

> Yellow highlited one are:
> - `9799680`
> - `S3A_SR_2_WAT____20220919T083843_20220919T084434_20220919T103642_0351_090_078______MAR_O_NR_005.SEN3`

**NOTE:** ignore the Word indentation, consider all single white spaces.

**Exercise:** Write a Python program that given the log message (reading it from the archive.log file), prints in the standard output the size and filename of the product.

**Example of output:**

Size: 9799680

Product Name: S3A_SR_2_WAT____20220919T083843_20220919T084434_20220919T103642_0351_090_078______MAR_O_NR_005.SEN3

**Description:** In this case scripts are in Task-3 folder. The ‘log_parse.py’ file consists of the python script which extract the information of the file size and the file name from the log message. The log message is in the ‘archive.log’ file.


## Task-4 : Users quota

1. Create a bash script able to read ‘user2‘ quota usage from a file named ‘quotas.txt’, returning the message ’[!] User quota exceeded’ if its value is greater than the ‘threshold’ value. 
   
   User quota is represented by ‘usedSpace’.

   ‘quotas.txt’ file content:
    
    ```bash
    username usedSpace threshold maxQuota lastUpdate
    user1 59 95 100 2024/01/22@08:30
    user2 72 95 100 2024/01/22@08:30
    user3 87 95 100 2024/01/22@08:30
    user4 45 95 100 2024/01/22@08:30
    ```
    **Description:** In this case, `users_quota.sh` file contains the bash script which will read the content of the file ‘quotas.txt’. To do this, I have used the while loop and read the lines and extracts the `username`, `usedSpace`, `threshold`. Then, it checks if the username is 'user2'. If it is, the script compares the used space with the threshold. If the used space exceeds the threshold, it prints a message indicating that the user quota has been exceeded. Otherwise, it prints a message indicating that the user quota is within the threshold.

2. How would you automate the execution of the script, so that it would be run every 35 minutes?
   
    **Description:** 
    - Open the crontab file for editing by running the following command in your terminal:
      ```
      crontab -e
      ```
    - Add the following line to the crontab file to schedule the script to run every 35 minutes:
      ```
      */35 * * * * /path/to/users_quota.sh >> /path/to/cronjob.log 2>&1
      ```
      Here, I intend to keep a log of the cronjob in the cronjob.log file. In each 35 minutes, the `users_quota.sh` script will be executed and then the output generated (standard output or error messages) by the script will be  redirected to a log file named `cronjob.log`. This ensures that any output generated by the script is captured and logged for later review or analysis. 


