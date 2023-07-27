def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    for i in range(n):
        if (deliveries[i] != 0) or (pickups[i] != 0):
            maxnum1 = cap
            maxnum2 = cap
            answer += 2 * (n - i)
            for j in range(n):
                if maxnum1 != 0:
                    if deliveries[j] <= maxnum1:
                        maxnum1 -= deliveries[j]
                        deliveries[j] = 0
                    else:
                        deliveries[j] = deliveries[j] - maxnum1
                        maxnum1 = 0
                
                if maxnum2 != 0:
                    if pickups[j] <= maxnum2:
                        maxnum2 -= pickups[j]
                        pickups[j] = 0
                    else:
                        pickups[j] = pickups[j] - maxnum2
                        maxnum2 = 0

    return answer