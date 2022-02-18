log_file = open("um-server-01.txt") # open('') is accessing the .txt and storing the info in it to a variable called log_file


def sales_reports(log_file):        # A function called sales_report which takes in a single parameter called log_file
    for line in log_file:           # A for loop which defines each line/row of data in an object as 'line' and loops over the rows of data in the file log_file
        line = line.rstrip()        # Removes whitespace from the right side of a line.
        day = line[0:3]             # Splices/or makes a shallow copy the contents of line starting from index 0 to just before index 3. So 0 to 2.
        if day == "Mon":            # A conditional which checks to see if the variable day is strictly equal to 'Tue'.
            print(line)             # Action performed after conditional statement is to send the contents of the line variable to the display or console.
    log_file.seek(0,0);

sales_reports(log_file)             # The function 'sales_reports is invoked and passed the variable 'log_file'.


#Changes conditional to check for orders on "Mon" instead of "Tues"/

## Extra Credit
def melons_over_10(log_file):
    for rows in log_file:
        split = rows.split(' ');
        if int(split[2]) > 10:
            print(' '.join(split));


melons_over_10(log_file)
