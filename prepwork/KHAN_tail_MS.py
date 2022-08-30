#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #imports module
filename = sys.argv[1] #defines variable "filename" as the first input of the command
if len(sys.argv) > 2: #checks if user has requested the line number defined as the second input of the command
  n_lines = int(sys.argv[2]) #if they have done so, "n_lines" is defined as the integer number of lines requested in the input
else: #if the user has not requested the line number
  n_lines = 10 #set the default line number in "n_lines" to 10
f = (open(filename).read()) #defines "f" as the whole, read file
line_list = f.splitlines() #defines "line_list" as a list of each line as a member of said list, separated by line breaks using splitlines
length = len(line_list) #measures the length of the list and defines variable "length" using the integer size of the list
for i in range(length-n_lines, length): #define "i" as the list length requested starting from the bottom of the list, doing so by using range start as "length" minus the lines requested in "n_lines" and range stop as the total list length
    print (line_list[i]) #prints the matching "line_list" content requested for each requested index in "i"

# This is a great script. I really like your use of splitlines and range. The
# only feedback I have is about readability. First, including blank lines to
# break your code up into functional blocks is really helpful for readability.
# Also, putting longer comments on the own lines. Beyond that, it's clear you
# have a good grasp of what you're doing. Excellent job and keep it up! - Mike