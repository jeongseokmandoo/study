def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    for i in range(n):
        if (deliveries[i] != 0) or (pickups[i] != 0):
            maxnum = cap
            answer += 2 * (n - i)
            for j in range(n):
                if maxnum == 0:
                    break
                if deliveries[j] <= maxnum:
                    maxnum -= deliveries[j]
                    deliveries[j] = 0
                else:
                    deliveries[j] = deliveries[j] - maxnum
                    maxnum = 0
            maxnum = cap
            for k in range(n):
                if maxnum == 0:
                    break
                if pickups[j] <= maxnum:
                    maxnum -= pickups[j]
                    pickups[j] = 0
                else:
                    pickups[j] = pickups[j] - maxnum
                    maxnum = 0
    return (answer)