#include <stdio.h>
#include "demo.h"

int main (){
    int a=10, b=20, c, d, e, f, g;

    c=sum(a,b);
    d=square(a);
    e=diff(b,a);
    f=product(a,b);
    g=division(b,a);

    printf("Sum is : %d\n", c);
    printf("Square is : %d\n", d);
    printf("Difference is : %d\n", e);
    printf("Product is : %d\n", f);
    printf("Division is : %d\n", g);

    return 0;
}