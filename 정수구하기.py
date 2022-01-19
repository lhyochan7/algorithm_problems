import random

def add(a, b):
    sum = 0
    for num in range(a,b+1):
        sum += num
    return sum

def multiply(a,b):
    sum = 1
    for num in range(a, b+1):
        sum *= num
    return sum

def randomAddMult(n):
    add_sum = 0
    mult_sum = 1
    for num in range(n):
        rand = random.randint(1,10)
        print(rand)
        add_sum += rand
        mult_sum *= rand

    return add_sum, mult_sum


if __name__ == "__main__":
    a, b, n = input(), input(), input()
    a, b = int(a), int(b)
    add_sum = add(a,b)
    mult_sum = multiply(a,b)
    rand_add_sum, rand_mult_sum = randomAddMult(n)

    print("rand add sum = ", rand_add_sum)
    print("rand mult sum = ", rand_mult_sum)
    print("add sum = ", add_sum)
    print("mult sum = ", mult_sum)
    print("a = %d, b = %d" %(a, b))
