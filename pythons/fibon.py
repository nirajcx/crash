# check the valid nth term
nth = int(input('Enter the nth term: '))
n1 = int(input('Enter the 1st term'))
n2 = int(input('Enter the 2nd term'))
count =0
l=[]
if nth <= 0:
    print('Enter the positive value greater than 0')
elif nth == 1:
    print('Fibonacc of 1 is ', n1)
else:
    while count<nth:
        l.append(n1)
        res=n1+n2
        n1=n2
        n2=res
        count+=1
print('The fibonacc sequence is ',l)
