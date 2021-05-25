#include<stdio.h>

int main(void)
{
  int a = 0;
  for(int i = 0; i < 10000000000; i++)
  {
    a++;
  }
  printf("a: %d\n",a);
}

