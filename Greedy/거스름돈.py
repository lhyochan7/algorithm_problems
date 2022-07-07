n = 1260 
count = 0

coin_types = [500,100,50,10] 

for coin in coin_types:
    print("n//coin", n//coin)
    count += n // coin
    print("count", count)
    n %= coin
    print("n", n)
    
print(count)