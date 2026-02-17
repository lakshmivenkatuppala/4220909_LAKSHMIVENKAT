#include <stdio.h>

/* Arthematic operators
+	Addition	Adds together two values	x + y	
-	Subtraction	Subtracts one value from another	x - y	
*	Multiplication	Multiplies two values	x * y	
/	Division	Divides one value by another	x / y	
%	Modulus	Returns the division remainder	x % y	
++	Increment	Increases the value of a variable by 1	++x	
--	Decrement	Decreases the value of a variable by 1	--x */
int main(){
    int x = 10;
    int y = 3;

    printf("%d\n", x + y);
    printf("%d\n", x - y);
    printf("%d\n", x * y);
    printf("%d\n", x / y);
    printf("%d\n", x % y); 

    int z = 5;
    ++z;
    printf("%d\n", z); 
    --z;
    printf("%d\n", z);
    return 0;
}