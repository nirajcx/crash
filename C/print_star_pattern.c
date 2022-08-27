#include <stdio.h>
int main()
{
    printf("Enter the numbers of * to print\n");
    int k, l;
    scanf("%d", &k);
    printf("ENter the 0 for positive or 1 for reverse\n");
    scanf("%d", &l);
    if (l == 0)
    {
        for (int i = 0; i <= k; i++)
        {
            printf("\n");
            for (int j = 0; j < i; j++)
            {
                printf("*");
            }
        }
    }
    else if (l == 1)
    {
        for (int i = k; i >= 0; i--)
        {
            printf("\n");
            for (int j = 0; j < i; j++)
            {
                printf("*");
            }
        }
    }
}