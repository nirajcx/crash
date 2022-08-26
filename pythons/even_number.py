even_numbers = list(range(2, 11, 2))
print(even_numbers)
eve = [valu**2 for valu in range(1, 11)]
print(eve)
print(type(eve))
l = []
print('odd number')
for a in range(1, 21):
    if a%2 != 0:
        print(a)
        l.append(a)
print(l)
