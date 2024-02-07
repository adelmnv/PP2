def solve(numheads, numlegs):
    is_found = False
    for numchikens in range(numheads+1):
        numrabbits = numheads - numchikens
        if(numchikens*2 + numrabbits*4) == numlegs:
            is_found = True
            break
    if is_found:
        print(f"Number of chickens: {numchikens}")
        print(f"Number of rabbits: {numrabbits}")
    else:
        print("Solution is not found")