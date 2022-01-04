def solution(array, commands):
	answer = []
	slice = []

	for command in commands:
			
		i, j, k = command[0], command[1], command[2]
		
		slice = array[command[0]-1:command[1]]
		
		#print(slice)
		
		slice.sort()

		answer.append(slice[command[2]-1])

		#print(command[0], command[1], command[2])

	return answer


array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

print(solution(array, commands))
