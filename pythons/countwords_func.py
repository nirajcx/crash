def countwords(book):
    try:
        with open(book) as de:
            a = de.read()
    except FileNotFoundError:
        #print(book, " Not found")
        pass
    else:
        b = a.split()
        num = len(b)
        print(num, "Words were there in",book)


listof=['car.py','alice.txt','dog_class.py','arbi.py','abc.txt']
for i in listof:
    countwords(i)
