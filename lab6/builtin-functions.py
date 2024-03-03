#1 
nums = [1,2,3,4,5]
p = 1
s = "*".join(map(str,nums))
res = eval(s)
print(res)

#2
def islower(x):
    return x.islower()

def isupper(x):
    return x.isupper()

text = "HeLLo"
lower_num = len(list(filter(islower,text)))
upper_num = len(list(filter(isupper,text)))
print(f"number of upper case letters = {upper_num} and lower case letters = {lower_num}")

#3
text = "mum"
res = eval('text==text[::-1]')
print(res)

#4
import time
num = int(input())
ms = int(input())
time.sleep(ms/1000)
print(f"Square root of {num} after {ms} miliseconds is {pow(num,0.5)}")

#5
tpl = (True,True,1)
print(all(tpl))
