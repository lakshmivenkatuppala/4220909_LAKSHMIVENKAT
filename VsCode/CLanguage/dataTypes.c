// int	2 or 4 bytes	Stores whole numbers, without decimals	1
// float	4 bytes	Stores fractional numbers, containing one or more decimals. Sufficient for storing 6-7 decimal digits	1.99
// double	8 bytes	Stores fractional numbers, containing one or more decimals. Sufficient for storing 15 decimal digits	1.99
// char	1 byte	Stores a single character/letter/number, or ASCII values

/* Format Specifier	    Data Type
    %d or %i	        int	
    %f or %F	        float	
    %lf	                double	
    %c              	char	
    %s	                Used for strings (text), which you will learn more about in a later chapter */

#include <stdio.h>

int main(){
    int myNum = 1000;
    double dNum = 19.99;
    float myFloatNum = 5.75;

    // C Decimal Precision
    printf("%d\n", myNum);
    printf("%f\n", myFloatNum);   // Default will show 6 digits after the decimal point
    printf("%.1f\n", myFloatNum); // Only show 1 digit
    printf("%.2f\n", myFloatNum); // Only show 2 digits
    printf("%.4f\n", myFloatNum);   // Only show 4 digits
    printf("%lf\n", dNum);

    // C The sizeof Operator
    printf("%zu\n", sizeof(int));
    printf("%zu\n", sizeof(float));
    printf("%zu\n", sizeof(double));
    printf("%zu\n", sizeof(char));

    // C Extended Types
    printf("Size of int: %zu bytes\n", sizeof(int));
    printf("Size of double: %zu bytes\n", sizeof(double));
    printf("Size of short int: %zu bytes\n", sizeof(short int));
    printf("Size of unsigned int: %zu bytes\n", sizeof(unsigned int));
    printf("Size of long int: %zu bytes\n", sizeof(long int));
    printf("Size of long long int: %zu bytes\n", sizeof(long long int));
    printf("Size of unsigned long long int: %zu bytes\n", sizeof(unsigned long long int));
    printf("Size of long double: %zu bytes\n", sizeof(long double));

    return 0;
}