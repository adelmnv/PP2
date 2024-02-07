from converting_functions import grams_to_ounces, fahrenheit_to_centigrade
from classic_puzzle import solve
from filter_func import filter_prime
from string_funct import reversed_words, palindrome, generate_permutations
from list_funct import has_33, spy_game,unique_elements
from geom_func import sphere_volume, histogram
from game import guess_the_num
#1
print(grams_to_ounces(100))
print("--------------")

#2
print(fahrenheit_to_centigrade(86))
print("--------------")

#3
solve(35,94)
print("--------------")

#4
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(num))
print("--------------")

#5
s = "abc"
generate_permutations(s)
print("--------------")

#6
s = "We are ready"
print(*reversed_words(s))
print("--------------")

#7
has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])
print("--------------")

#8
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
print("--------------")

#9
radius = 5.0
result = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is {result:.2f}")
print("--------------")

#10
nums = [1,1,2,3,4,4,4,5,6,7,8,9]
print(*unique_elements(nums))
print("--------------")

#11
palindrome("mum")
palindrome("granny")
print("--------------")

#12
histogram([4, 9, 7])
print("--------------")

#13
guess_the_num()