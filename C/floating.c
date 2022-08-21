#include <stdio.h>
#include <math.h>
float average(float a, float b, float c);
int main()
{
    float  a, b, c, d;
    printf("Enter the three number:\n");
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);
    d=average(a, b, c);
    printf("\n %f",d);
    return 0;
}
float average(float a, float b, float c)
{
    float result;
    result = (a + b + c)/3;
    return result;
}