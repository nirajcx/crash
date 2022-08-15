from asyncio import create_subprocess_exec


cube = []
for a in range(1, 11):
    cube.append(a**3)
print(cube)
c = [cub**3 for cub in range(1, 11)]
print(c)
