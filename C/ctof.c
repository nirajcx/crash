#include <stdio.h>
float ctof(float temp);
float main()
{
    float a, result;
    printf("Enter the temp");
    scanf("%f", &a);
    result = ctof(a);
    printf("\n Enter the temp %f", result);
}
float ctof(float temp)
{
    float result;
    result = (temp *9/5) + 32;
    return result;
}