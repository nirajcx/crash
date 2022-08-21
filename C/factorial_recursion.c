#include <stdio.h>
int factorial(int x);
int factorial_iterative(int x);
int main()
{
    int a;
    printf("Enter the number for factorial\n");
    scanf("%d", &a);
    printf("The value of factorial %d is %d,\n", a, factorial(a));
    printf("The value of factorial %d\n", factorial_iterative(a));
    return 0;
}
int factorial(int x)
{
    if (x == 0 || x == 1)
        return 1;
    else
        return (x * factorial(x - 1));
}
int factorial_iterative(int x)
{
    int f = 1;
    for (int i = 1; i <= x; i++)
    {
        f = f * i;
    }
    return f;
}