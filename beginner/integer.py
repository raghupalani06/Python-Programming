N = int(input(" "))
Count = 0
while(N > 0):
    N = N// 100
    Count = Count + 1
 
print("\n Number of Digits in a Given Number = %d" %Count)
