favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " +name.title() + ", I see your fav language is " + favorite_languages[name].title())
print(favorite_languages['jen'])
if 'erin' not in favorite_languages.items():
    print("Erin, please take our poll!")
for a in sorted(favorite_languages):
    print(a.title(), "Thanks for participating")