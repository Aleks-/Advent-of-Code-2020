import numpy as np
import re

Part_one = False

valid = 0
with open('Day_2.txt') as f:
    for line in f:
        pattern = re.compile(r'(\d+)\W(\d+)\s([a-z])\W\s(\w*)')    # regex for numbers
        matches = pattern.findall(line)
        lowest = int(matches[0][0])
        highest = int(matches[0][1])
        letter = matches[0][2]
        password = matches[0][3]

        if Part_one:
                
            num_of_letters = password.count(letter)
            
            if lowest <= num_of_letters <= highest:
                valid += 1
            else:
                None
        
        if not Part_one:
            x = password[lowest-1] == letter
            y = password[highest-1] == letter
            if (not(x and y) and (x or y)):
                valid += 1
            else:
                None      
            
print(valid)
        

