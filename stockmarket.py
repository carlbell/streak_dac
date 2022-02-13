import sys
import math 
import os

"""
to run, just run "python3 stockmarket.py *inputfile* *outputfile*"
replacing *inputfile* and *outputfile* with the paths of the
input and output files respectively

thanks

Aidan Garton and Carl Bell

"""

def main():
    # remove output file if already exists
    # i.e., clear previous output
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])

    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'a')

    # load in lines of file into list
    lines = [line.rstrip() for line in input_file]
    # sequence to pass to the algorithm
    input_sequence = lines[1:]

    # run algorithm on input
    length, start_index, output_sequence = longest_run(input_sequence)

    # write length of longest non-decreasing substring and start index to output file
    output_file.write(str(length) + "\n")
    output_file.write(str(start_index) + "\n")
    
    # write longest found nondecreasing subsequence to output
    for element in output_sequence:
        output_file.write(element + "\n")
    
    input_file.close()
    output_file.close()


#finds the longest run of non-decreasing numbers which 
# goes through the middle of an arraydef mid_run(input_array):
def mid_run(input_array):
    mid = int(math.floor(len(input_array) / 2)) - 1
    
    prev = input_array[mid]
    i = 1

    current = input_array[mid-i]
    while prev >= current: 
        # iterate backwards through the list starting from the middle
        #  until we find a pair of days where the stock price decreased

        prev = input_array[mid-i]
        i+=1
        if i > mid:
            # if the whole left side of the list is non-decreasing
            break
        current = input_array[mid-i]
    start_of_run = mid - (i-1) # store the index of the last i that
                        # continued the streak of non-decreasing days
                        
    #print(str(i) + " " +str(mid)+" !!!!!!!!!!! "+str(start_of_run))
    
    #now iterate through the right half to find how far 
    #  the non-decreasing streak goes on the right if at all
    prev = input_array[mid]
    j = 1
    current = input_array[mid+j]
    while prev <= current: 
        # iterate forward through the list starting from the middle
        #  until we find a pair of days where the stock price decreased
        #print("j " + str(j))
        #print ("prev " + str(prev))
        #print ("current " + str(current))
        prev = input_array[mid+j]
        j+=1
        if j > ((len(input_array)/2)-1):
            # if the whole right side of the list is non-decreasing
            break
        current = input_array[mid+j]
    end_of_run = mid + (j - 1) # store the index of the last j that
                        # continued the streak of non-decreasing days
    streak = input_array[start_of_run : end_of_run + 1]
    #print("end of RUN!!!" + str(end_of_run))
    #print(streak)
    
    # return the length of the streak crossing the middle, the starting index
    # and the streak itself as a list
    return (len(streak), start_of_run+1, streak) 

    
    

def longest_run(input_array):
    if len(input_array) == 1:
        # base case, an array of length 1 is a non-decreasing run of 1 element
        return (1, 1, [input_array[0]])
    if len(input_array) == 2:
        if input_array[0] <= input_array[1]:
        # base case, an array of length 2 is a non-decreasing run of 2 elements
        #  if its first element is less than or equal to its second element
            return (2, 1, input_array)
        return (1, 1, [input_array[0]])
        
    # otherwise we will find the maximum run of non-decreasing by checking the
    #  longest non-decreasing on the left, on the right, and crossing the middle
    mid = int(math.floor(len(input_array)/2))
    left = input_array[:mid] #the first half of the array
    right = input_array[mid:] #the second half of the array

    #find the length of the longest run that crosses the middle
    mid_run_result = mid_run(input_array)
    if mid_run_result[0] >= mid:
        # if the run of non-decreasing days going through the
        #middle is longer than either half it is definitely longer
        #than the longest non-decreasing streak in either half
        return mid_run_result
    left = longest_run(left)
    right = longest_run(right)
    right = (right[0], right[1]+mid, right[2])

    # check if the streak going throught the middle is the longest
    if mid_run_result[0] >= left[0] and mid_run_result[0] >= right[0]:
        return mid_run_result
        
    # check if left is longer than right
    if left[0] >= right[0]:
        return left
        
    # otherwise right has to be the longest
    return right

if __name__ == '__main__':
  main()