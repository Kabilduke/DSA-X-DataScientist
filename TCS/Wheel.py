def tcs(V, W):
    if(W & 1) == 1 or W < 2 or W<=V:
        print("Invalid Input")
    else:
        x =((4*V) - W)//2

    return "TW = {0} FW = {1}".format(x, V-x)

V = 200
W = 540
result = tcs(V, W)
print(result)
