# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to
# Returns

# string: a single string with newline characters ('\n') where the breaks should be

def wrap(string, max_width):
    s=""
    for i in range(len(string)):
        if i!=0 and i%max_width==0:
            s=s+"\n"+string[i]
        else:
            s=s+string[i]
    return s