# Which starting number, under one million, produces the longest chain

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False

def create_sequence(x):
    collatz_sequence = [x]
    while x != 1:
        if is_even(x):
            x = x/2
        else:
            x = ((3*x)+1)
        collatz_sequence.append(x)
    # print(collatz_sequence)
    return collatz_sequence

num = 999999

greatest_len = 0
greatest_num = None

for n in range(1,1000000):
    sequence = create_sequence(n)
    length = len(sequence)
    if length > greatest_len:
        greatest_len = length
        greatest_num = n

print(greatest_len, " ", greatest_num)
