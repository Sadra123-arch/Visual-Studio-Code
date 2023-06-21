def comput_power(base,power):
    resault=1
    for i in range(power):
        resault=resault*base
    
    return resault

base = int(input("Insert Base : "))
power = int(input("Insert Power : "))
print(comput_power(base,power))

import cv as cv2
