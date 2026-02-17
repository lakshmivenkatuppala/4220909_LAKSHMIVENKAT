/* Comparison Operators 
Operator	Name	                    Example	Description	Try it
==	        Equal to	                x == y	Returns 1 if the values are equal	
!=	        Not equal	                x != y	Returns 1 if the values are not equal	
>	        Greater than	            x > y	Returns 1 if the first value is greater than the second value	
<	        Less than	                x < y	Returns 1 if the first value is less than the second value	
>=	        Greater than or equal to	x >= y	Returns 1 if the first value is greater than, or equal to, the second value	
<=	        Less than or equal to	    x <= y	Returns 1 if the first value is less than, or equal to, the second value
*/
#include <stdio.h>

int main(){
    int age = 18;
    printf("%d\n", age >= 18); // 1 (true), old enough to vote
    printf("%d\n", age < 18);  // 0 (false)

    int passwordLength = 5;
    printf("%d\n", passwordLength >= 8); // 0 (false), too short
    printf("%d\n", passwordLength < 8);  // 1 (true), needs more characters

    return 0;
}