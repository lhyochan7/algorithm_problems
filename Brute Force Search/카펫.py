def solution(brown, yellow):
    answer = []

    totalArea = brown + yellow

    opt = [(yellow//i,i) for i in range(1, int(yellow)+1) if yellow % i == 0]


    for r, h in opt:
        if ((r+2) * (h+2) == totalArea) and int(r) >= int(h):
            return([r+2, h+2])