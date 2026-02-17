/* Logical Operators 
&& 	AND	x < 5 &&  x < 10	Returns 1 if both statements are true	
|| 	OR	x < 5 || x < 4	Returns 1 if one of the statements is true	
!	NOT	!(x < 5 && x < 10)	Reverse the result, returns 0 if the result is 1	
 */

#include <stdio.h>

int main(){
    int isLoggedIn = 1;
    int isAdmin = 0;

    printf("Regular user: %d\n", isLoggedIn && !isAdmin);
    printf("Has access: %d\n", isLoggedIn || isAdmin);
    printf("Not logged in: %d\n", !isLoggedIn);
    return 0;
 }