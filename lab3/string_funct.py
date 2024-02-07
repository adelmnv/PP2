def generate_permutations(s, current=''):
    if not s:
        print(current)
    else:
        for i in range(len(s)):
            remaining_chars = s[:i] + s[i+1:]
            generate_permutations(remaining_chars, current + s[i])
    

def reversed_words(s):
    words = s.split()
    reversed = words[::-1]
    return reversed

def palindrome(s):
    reversed_s = s[::-1]
    if s == reversed_s:
        print(f"string '{s}' is palindrome")
    else:
        print(f"string '{s}' is NOT palindrome")
    
