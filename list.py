frmds = ['google', 'pc', 'youtube', 'games']
print(frmds[0].title())
print(frmds[1].title())
print(frmds[2].title())
print(frmds[3].title())
print(frmds[0].title() + ' ' + 'You are my frnd')
print(frmds[1].title() + ' ' + 'You are my frnd')
print(frmds[2].title() + ' ' + 'You are my frnd')
print(frmds[3].title() + ' ' + 'You are my frnd')
frmds[3] = 'Parrot'
frmds.append('bike')
print(frmds)
bikes = []
bikes.append("yamaha")
bikes.append("honda")
bikes.append("hero")
bikes.append("suzuki")
bikes.insert(1, "KTM")
print(bikes)
del bikes[3]
print(bikes)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
