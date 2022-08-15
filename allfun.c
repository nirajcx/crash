#include <stdio.h>
#include <math.h>
int squar(int side);
float circle(float radius, float pi);
int rectangle(int l, int b);
int main()
{
    int side = 4;
    float radius = 5;
    int l = 2;
    int b = 3;
    float pi = 3.14;
    squar(side);
    printf("The Area of the squar is : %d\n", squar(side));
    circle(radius,pi);
    printf("The area of the circle is :%f\n", circle(radius, pi));
    rectangle(l,b);
    printf("The area of the recangle is :%d\n", rectangle(l, b));

    return 0;
}
int squar(int side)
{
    return side * side;
}
float circle(float radius, float pi)
{
    return radius * radius * pi;
}
int rectangle(int l, int b)
{
    return l * b;
}