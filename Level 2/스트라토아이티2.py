def solution(prices):

    answer = 0
    maxPrice = prices[0]
    minPrice = prices[0]

    for price in prices:
        if price < minPrice:
            minPrice = price
            maxPrice = 0

        if price > maxPrice:
            maxPrice = price

            if answer < maxPrice - minPrice:
                answer = maxPrice - minPrice
        
        print("price = %d, minPrice = %d, maxPrice = %d, answer = %d" %(price, minPrice, maxPrice ,answer))
    return answer



prices = [[3,4,1,5,4], [3,13,2,9,6], [5,13,1,10,2]]

for price in prices:
    print(solution(price))