paths='D:/9S/pi_digi.txt'
with open(paths) as fdi:
    contents = fdi.read()
    print(contents.rstrip())
