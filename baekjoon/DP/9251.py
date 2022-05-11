first = input()
second = input()

height = len(first) 
width = len(second)

table = [[0] * (width+1) for _ in range(height + 1)]

for i in range(1, height+1):
    for j in range(1, width+1):
        if i == 0 or j == 0:
            if first[i] == second[j]:
                table[i][j] = 1
            else:
                table[i][j] = 0
        else:
            if first[i-1] == second[j-1]:
                #table[i][j] = max(table[i][j-1], table[i-1][j]) + 1
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])


for t in table:
    print(t)

print(max(table[height]))