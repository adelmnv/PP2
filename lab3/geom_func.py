import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def histogram(nums):
    for i in range(len(nums)):
        num = nums[i]
        for j in range(num):
            print("*",end="")
        print()