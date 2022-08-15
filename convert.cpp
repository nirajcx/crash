// Convert.cpp
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	char c;
	int n,t1,t2,sum=0;
	n=16;
	cout<<endl;
	int array[n],dec[n];
	for(int i=0; i<n; )
	{
		cout<<"Enter Binary Code "<<i+1<<" : ";
		cin>>array[i];
		t1=array[i];
		while(t1!=0)
		{
			t2=t1%10;
			t1=t1/10;
			if(t2>1)
			{
				c='n';
				break;
			}
			else
				c='y';
		}
		if(c=='y')
			i++;
		else 
			cout<<"Invalid Input"<<endl;
	}
	cout<<"\n\nBinary codes : \n";
	for(int i=0; i<n; i++)
	{
		cout<<array[i]<<" ";
	}
	cout<<"\n\nIts Decimals : \n";
	for(int i=0; i<n; i++)
	{
		t1=array[i];
		for(int j=0; ;j++)
		{
			t2=t1%10;
			if(t2==1)
				sum+=pow(2,j);
			t1=t1/10;
			if(t1==0)
				break;
		}
		dec[i]=sum;
		cout<<dec[i]<<" ";
		sum=0;
	}
	cout<<endl;
	return 0;
}
