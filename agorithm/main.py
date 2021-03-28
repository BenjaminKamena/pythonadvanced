#for i in range(100):
  #print(i)

#for i in range(100):
    #for j in range(100):
        #print(i, j)

arr = [-1, 2, 4, -3, 5, 2, -5, 2]

best = 0
for i in arr:
    for j in arr:
        sum = 0
        for k in arr:
            sum += k
        best = max(best, sum)
print(best)

best = 0
for i in arr:
    sum = 0
    for j in arr:
        sum += j
        best = max(best, sum)
print(best)

best, sum = 0, 0
for i in arr:
    sum = max(i, sum + i)
    best = max(best, sum)
print(best)






