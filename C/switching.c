#include <stdio.h>
void main()
{
    int a, money;
    scanf("%d", &a);
    switch (a)
    {
    case 1:
        printf("value is one");
        scanf("%d", &money);
        switch (money)
        {
        case 10:
            printf("Welcome");
            break;

        default:
            break;
        }
        break;
    case 4:
        printf("4 has been enterd");
        break;
    case 9:
        printf("9 has been enterd");
        break;
    case 10:
        printf("10 has been enterd");
        break;
    }
}