#arr = [[0, 0, 0, 0], [0,0,0,0], [0,0,0,0]]
arr = []
for i in range(0,3):
	arr.append([])
for i in range(0,3):
	for j in range(0,4):
		arr[i].append(0)

print(arr)

del arr[2][0]
arr[2].append(10)

del arr[2][0]
arr[2].append(11)

del arr[0][0]
arr[2].append(12)

arr[0][2] = 4
print(arr)