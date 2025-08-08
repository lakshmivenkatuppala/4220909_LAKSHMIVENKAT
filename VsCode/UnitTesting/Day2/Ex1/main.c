#include <stdio.h>
#include "demo.h"
#include "unity.h"

void setUp(){}
void tearDown(){}

void test_sum(){
    TEST_ASSERT_EQUAL(3, sum(1,2));
    TEST_ASSERT_EQUAL(10, sum(3,7));
}

void test_diff(){
    TEST_ASSERT_EQUAL(5, diff(7,2));
    TEST_ASSERT_EQUAL(1, diff(11,10));    
}

void test_square(){
    TEST_ASSERT_EQUAL(9, square(3));
    TEST_ASSERT_EQUAL(49, square(7));
}

void test_product(){
    TEST_ASSERT_EQUAL(9, product(3,3));
    TEST_ASSERT_EQUAL(56, product(7,8));
}

void test_division(){
    TEST_ASSERT_EQUAL(9, division(27,3));
    TEST_ASSERT_EQUAL(7, division(49,7));
}


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

    UNITY_BEGIN();
    RUN_TEST(test_sum);
    RUN_TEST(test_diff);
    RUN_TEST(test_square);
    RUN_TEST(test_product);
    RUN_TEST(test_division);

    return UNITY_END();
}