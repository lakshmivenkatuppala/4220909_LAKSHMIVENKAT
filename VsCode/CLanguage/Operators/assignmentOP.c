/* Assignment Operators 
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
*/
#include <stdio.h>
int savings = 100; 
int main(){
    savings += 50;
    printf("Total savings: %d\n", savings);
    savings-=10;
    printf("Total savings: %d\n", savings);
    savings*=2;
    printf("Total savings: %d\n", savings);
    savings/=5;
    printf("Total savings: %d\n", savings);
    savings%=5;
    printf("Total savings: %d\n", savings);
    return 0;
    }