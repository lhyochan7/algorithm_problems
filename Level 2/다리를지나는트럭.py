def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while bridge:
        time += 1
        bridge.pop(0)
        
        if truck_weights:
            # if bridge can hold the next truck weight
            if sum(bridge) + truck_weights[0] <= weight:
                # add the next truck weight to the bridge
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
            
    return time