// QUESTION: Define a function to take a integer and return even or odd

#include<stdio.h>
int main()
{
	int number,ans;
	scanf("%d",&number);   //take number as a input
	even_or_odd(number);
	//printf("\n%d",ans);
	return 0;
}

// Function to determine a whether a number is even or odd
int even_or_odd(int num)
{
	if (num%2==0)
		printf ("Even");
	else
		printf ("Odd");
}
