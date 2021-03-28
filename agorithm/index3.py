arr = [1, 3, 8, 2, 9, 2, 5, 6]

for i, j in enumerate(arr):
    for a, b in enumerate(arr[: -1]):
        if arr[a] > arr[a+1]:
            arr[a], arr[a+1] = arr[a+1], arr[a]
print(arr)

names = ['A', 'N', 'T', 'H', 'O', 'N', 'Y']

#traversing an array
#for i in name:
   # print(i)

#data structure
#arr.pop()
#print(arr)

#arr.append(1)
#print(arr)

s = {1, 2, 3, 4, 5, 2}
#print(s)

#s.remove(5)
#print(s)

#s.add(5)
#print(s)

#print(len(s))

#dictionary = {1: 2, 2: 3}
#print(dictionary)
#print(dictionary.keys())
#print(dictionary.values())
#print(dictionary.items())

#for i, j in dictionary.items():
 #   print(i, j)

#print(2 in dictionary)
#print(3 in dictionary)

