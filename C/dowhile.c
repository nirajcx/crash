#include <stdio.h>
void main()
{
    printf("Enter the number \a");
    int a,i=1;
    scanf("%d", &a);
    do
    {
        printf("%d x %d = %d\n",a,i,a*i);
        i++;

    } while (i<=10);
    
    
}

