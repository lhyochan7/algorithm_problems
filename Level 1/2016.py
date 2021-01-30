def solution(a,b):
	answer =''
	
	date = ['FRI','SAT','SUN','MON','TUE','WED','THU']
	month = [31,29,31,30,31,30,31,31,30,31,30,31]

	days = sum(month[:a-1])
	days += (b-1)

	answer = date[days%7]

	return answer

print(solution(5,24))
print(solution(12,31))
print(solution(6,12))
