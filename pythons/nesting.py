aliens = []
for new_aliens in range(30):
    new_aliens = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aliens)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))
for alien in aliens[0:3]:
    if alien['color'] == 'green':
     alien['color'] = 'yellow'
     alien['speed'] = 'medium'
     alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print("...")