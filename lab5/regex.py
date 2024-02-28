import re

# with open('row.txt', 'r', encoding='utf-8') as file:
#     content = file.read()

#1
words = ['abb','abc','acc', 'bbd', 'bd']
p = re.compile(r'ab*')
res = []
for w in words:
    if p.match(w):
        res.append(w)
print(res)

#2
words = ['abbb','abb','ab']
p = re.compile(r'ab{2,3}')
res = []
for w in words:
    if p.match(w):
        res.append(w)
print(res)

#3
p = re.compile(r'[a-z]+_[a-z]+')
res = p.findall("abbb_ab B_zb yub_hill baa")
print(res)

#4
p = re.compile(r'[A-Z][a-z]+')
res = p.findall("Hello my name is Audio")
print(res)

#5
words = ['apple', 'arab', 'crab']
p = re.compile(r'[a-zZ-a]*a.*b$')
res = []
for w in words:
    if p.match(w):
        res.append(w)
print(res)

#6
p = re.compile(r'[ ,.]')
res = re.sub(p,':','Test string, hello, world.')
print(res)

#7
text = 'this_is_snake_case_string'
words = re.split('_',text)
for i in range(1,len(words)):
    words[i] = re.sub(r'^[a-z]', words[i][0].capitalize(),words[i])
res = ''.join(words)
print(res)

#8
text = 'HelloWorld'
words = re.split(r'(?=[A-Z])',text)
print(*words)

#9
text = 'Hello my name is Bob'
words = re.findall(r'[A-Z][a-z]*', text)

print(words)

#10
text = 'ThisIsCamelCaseString'
res = text[0].lower() + re.sub(r'(?=[A-Z])', '_', text[1:]).lower()
print(res)

