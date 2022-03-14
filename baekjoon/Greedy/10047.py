if __name__ == '__main__':
    n,k = map(int, input().split())

    coins = list()
    count = 0

    for i in range(n):
        coins.append(int(input()))

    coins = sorted(coins, reverse=True)

    for coin in coins:
        #print(coin)
        #print("k=", k)
        if k >= coin:
            while k >= coin:
                k -= coin
                count += 1

    print(count)