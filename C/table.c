#include <stdio.h>
void main()
{
    printf("Enter the number \a");
    int a;
    scanf("%d", &a);
    for (int i = 1; i <= 10; i++)
    {
        printf("%d x %d = %d\n ", a, i, a * i);
    }
}
