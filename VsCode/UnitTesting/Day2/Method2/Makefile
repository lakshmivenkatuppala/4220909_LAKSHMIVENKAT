object.o : main.c sum.c diff.c square.c product.c division.c
	gcc $^ -c

all : main.o sum.o diff.o square.o product.o division.o 
	gcc $^ -o $@

run : all 
	./all

clean :
	rm -rf all *.o *.out

# Special Variables:
# 1. $^ : Consider all the files present in the dependencies, seperated space.
# 2. $< : Consider only first file in the dependencies.
# 3. $@ : Represnting Target/ evaluates to all (executable file being generated named as all)