#include <math.h>
#include "prime.h"

/* Check integer input x is prime
 *
 * Returns:
 *    1 - prime
 *    0 - NOT prime
 *   -1 - undefined (i.e x < 2) 
 */
int is_prime(const int x){
  if(x < 2){
    return -1;
  }
  else if (x < 4){
    return 1; 
  }
  else if ((x % 2) == 0){
    return 0; 
  }

  for(int i = 3; i <= floor(sqrt((double) x)); i+= 2){
    if((x % i) == 0){
      return 0;
    }
  }

  return 1;
}

int next_prime(int x){
  while(is_prime(x) != 1){
    x++;
  }
  return x;
}
