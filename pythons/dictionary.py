alien_0 = {'color': 'Green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
shootpoints=alien_0['points']
print('Point for killing is '+ str(shootpoints))
alien_0['x_position']= 0
alien_0['y_position']= 25
print(alien_0)
alien_0['color']='yello'
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print('Sarah fav lang is '+ str(favorite_languages['sarah'].title()))