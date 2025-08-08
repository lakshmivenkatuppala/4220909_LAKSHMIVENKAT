# Unit Test:

Unit test is a software testing method where individual units or components of a software applications are tested.

The goal of Unit testing is to validate that each unit of the software performs as expected.

Advantages:
1. Helps to understand if code is working as expected or not.
2. Provides documentation.
3. Helps with finding bugs (Early bug detection).
4. Improved code quality.

Test Framework:
1. Provides Assertions, Checks and Matchers.
2. Helps with organising the code.
3. Provides report.
4. Automates the Execution.

eg: Google Test and Mock, Unity, Catch1, Catch2, Doctest, Boost, Test.

# Unity
1. Download Unity Framework Source Code:
sudo apt update
sudo install git
git clone https://github.com/ThrowTheSwitch/Unity.git

Note:
 - include unity Framework soure code i.e., unity.c, unity.h, unity_internals.h in your project directory

2. Include "unity.h" file in your testfile and in main file.

3. SetUp and tearDown functions:
setUp: executes before running each testcae.
tearDown: executes after running each test case.

4. Writing testcases:
void test_sum(){
    TEST_ASSERT_EQUAL(3, sum(1,2));
    TEST_ASSERT_EQUAL(10, sum(3,7));
}

5. Calling test case in main:
UNITY_BEGIN();
    RUN_TEST(test_sum);
return UNITY_END();

6. Makefile 
While compiling link unity.c and link unity.o to get executable files