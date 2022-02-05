def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[0], reverse=True)
    
    print(routes)
    now = routes[0][0]
    
    # start from the second route
    # set now as the min 진입 
    for route in routes[1:]:
        print(route)
        # if route is range of 진출
        if now <= route[1]:
            continue
        else:
            now = route[0]
            answer += 1
    
    return answer