#include<stdio.h>
void main(){
    int a[2][4];
    printf("Print array");
    for (int i = 0; i < 2 ;i++)
    {
        for(int j=0; j<4;j++)
        {
            printf("Enter the value of %d and %d",i,j);
            scanf("%d",&a[i][j]);
        }
    }
     for (int i = 0; i < 2 ;i++)
    {
        for(int j=0; j<4;j++)
        {
            
            printf("%d\n",a[i][j]);
        }
    }
    
}