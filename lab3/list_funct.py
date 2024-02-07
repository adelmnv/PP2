def has_33(nums):
    contain = False
    count = 0
    for i in nums:
        if i == 3:
            if contain:
                count+=1
            else:
                contain = True
        else:
            contain = False
    if count >=1:
        print("True")
    else:
        print("False")


def spy_game(nums):
    spy = []
    count_0 = 0
    count_7 = 0
    for i in nums:
        if i == 0 and count_0 < 2:
            spy.append(i)
        elif i == 7 and count_7 ==0:
            spy.append(i)
    if spy[0] == 0 and spy[1] == 0 and spy[2] == 7:
        print("True")
    else:
        print("False")

def unique_elements(elements):
    un_list = []
    for i in elements:
        if i in un_list:
            continue
        else:
            un_list.append(i)
    return un_list
