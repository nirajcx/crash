#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while (t--){
	    long int a,b;
	    scanf("%ld %ld",&a,&b);
	    if (a>=b)
	        printf("%ld\n",b);
	    else 
	        printf("%ld\n",a);
	    
	}
	
	return 0;
}

