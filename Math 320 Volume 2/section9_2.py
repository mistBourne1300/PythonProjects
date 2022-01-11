def bary_weights(points):
    weights = []
    for j in range(len(points)):
        wj = 1
        for k in range(len(points)):
            if j == k: continue
            wj *= points[j][0] - points[k][0]
        weights.append(1/wj)
    return weights
    
points = [(-1,2),(0,-4),(1,-6),(2,-16)]
print(bary_weights(points))
