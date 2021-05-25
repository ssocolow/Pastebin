#include <stdio.h>

int main(void)
{
  int a = 0;
  for(long i = 0; i < 21000000000; i++)
  {
    a = i;
  }
  printf("a: %d\n",a);
}
