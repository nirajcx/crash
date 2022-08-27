#include <stdio.h>
void printstr(char a[])
{
    int i = 0;
    while (a[i] != '\0')
    {
        printf("%c", a[i]);
        i++;
    }
}
int main()
{
    printf("String\n");
    char a[20];
    printf("Enter the string\n");
    gets(a);
    printf("Printing the string\n"); 
    printstr(a);
    printf("Printing the string Using printf\n"); 
    printf("%s\n",a); 
    printf("Printing the string Using puts\n"); 
    puts(a);

    return 0;
}
