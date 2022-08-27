#include<stdio.h>
int main(){
    printf("Arrays and pointers\n");
    int arr[]={1,2,3,5,6,7,8,9,10};
    int* ptr=arr;
    printf("value of array is %d\n",*(arr));
    printf("value of array is %d\n",*(ptr +1));
    printf("value of array is %d\n",*(ptr +2));
    return 0;
}