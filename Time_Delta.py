# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Input Format

# The first line contains , the number of testcases.
# Each testcase contains  lines, representing time  and time .

# Constraints

# Input contains only valid timestamps
# .
# Output Format

# Print the absolute difference  in seconds.

# Sample Input 0

# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0

# 25200
# 88200

from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(q, b):
    date1 = datetime.strptime(q, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(b, "%a %d %b %Y %H:%M:%S %z")
    difference=abs((date1-date2).total_seconds())
    return int(difference)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = str(time_delta(t1, t2))

        fptr.write(delta + '\n')

    fptr.close()
    print(delta)