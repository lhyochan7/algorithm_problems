def solution(numbers):
    answer = []
    tempSum = set()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            tempSum.add(sum)

    answer = list(tempSum)
    answer.sort()
    return answer



numbers = [2, 1, 3, 4, 1]

print(solution(numbers))
