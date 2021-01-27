def solution(new_id):
	answer = ''

	# stage 1
	new_id = new_id.lower()
	
	# stage 2
	for i in new_id:
		if i.isalpha() or i.isdigit() or i == '-' or i=='_' or i=='.':
			answer += i
	
	#print(new_id)
	

	# stage 3
	while '..' in answer:
		answer = answer.replace('..', '.')

	# stage 4
	if answer[0] == '.':
		answer = answer[1:]
	
	if answer[-1] == '.':
		answer = answer[:-1]

	# stage 5
	if answer == '':
		answer = 'a'

	# stage 6
	if len(answer) > 15:
		answer = answer[:15]
		if answer[-1] == '.':
			answer = answer[:-1]

	# stage 7
	while len(answer) < 3:
		answer += answer[-1]


	return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
new_id2 = "z-+.^."

print(solution(new_id))
print(solution(new_id2))
