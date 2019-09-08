# EEG-downsampler
 A python program that reads a csv file, detects its sample rate and downsamples its data.

## Assumptions
   This program expects a csv formatted file with no header line, each line containing an integer and a float separated by a comma.
   If the top line of your file contains column names, please delete them when using my program, they will be interpreted as data and a type error will occur.
   Such a compatible file is included in this repo called `csv_file.csv` and you can see how the file was made by looking at `csv_filemaker.py`

## Run Instructions
  1. Make sure you have python 3.5 or later installed (this is because I used type hinting to try and better satisfy the typed language preference, which is only available since 3.5)
  2. Open Terminal and navigated to the cloned repo and enter `py sample_rate.py "csv_file.csv"` or the linux equivalent (you can replace csv_file.csv with your own file's name). The program expects 1 command line argument, a string of the data set's file name.
  3. If you wish to write the new downsampled data to a file you can use `py sample_rate.py "csv_file.csv" > file_to_be_writen` just remember that the prompts to enter a new sample rate will be written in the new file, will not appear in the terminal and should be deleted from the top of the new file before analysing the new data.
