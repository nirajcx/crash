#include <stdio.h>
int swap(int *a, int *b)
{int temp;
temp=*a;
*a=*b;
*b=temp;
return 0;
}
int main()
{
    printf("Arrays and pointers\n");
    int a,b;
    a=12;
    b=66;
    printf("Value before changing %d and %d\n",a,b);
    swap(&a,&b);
    printf("Value after changing %d and %d\n",a,b);

    return 0;
}