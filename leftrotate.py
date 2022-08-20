arr = []
for i in range(0, int(input('Enter the number of element'))):
    t = int(input('enter elemet '))
    arr.append(t)
print('array before printing')
print(arr)

temp = []
shift = int(input('enter how much int to shift left '))

for y in range(0, shift):
    temp = arr[0]

for x in range(0, len(arr)-1):
    arr[x] = arr[x+1]
    arr[len(arr)-1] = temp

print('after the rotation')
print(arr)
