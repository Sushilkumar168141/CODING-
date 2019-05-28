#include<stdio.h>
int main()
{
    int number=20,ans=0;
    ans=solution(number);
}
int solution(int number) {
		// code here
    int sum=0,i=0;
    for (i=3;i<number;i++)
    {
      if(i%3==0 || i%5==0)
      {
          sum+=i;
          printf("\n number is %d and \n sum is  %d",i,sum);
      }
      /*
      if (i%3==0 && i%5==0)
      {
          sum-=i;
          printf("\n number is %d and \n sum -number is  %d",i,sum);
      }
      */
    }
    return sum;
}