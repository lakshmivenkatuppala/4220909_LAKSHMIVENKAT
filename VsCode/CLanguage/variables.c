#include <stdio.h>
#include <math.h>

int main(){
    int num=10; // int is used to read integer numbers
    float fnum=17.14; // float is used to read the decimal values
    char s='l'; // char stores a single character Characters are surrounded by single quotes
    printf("%d\n", num); // %d format specifier used to print integer value
    printf("%.2f\n", fnum); // %f format specifier used to print decimal value
    printf("%c\n", s); // %c format specifier used to print alphabet or character value
}
int area() {
    int length, width, area;
    length=10, width=20;
    area=length*width;
    printf("%d", area);
    return 0;
}