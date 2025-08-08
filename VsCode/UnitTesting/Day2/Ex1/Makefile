object.o : main.c sum.c diff.c square.c product.c division.c unity.c 
	gcc main.c sum.c diff.c square.c product.c division.c unity.c -c

all : main.o sum.o diff.o square.o product.o division.o unity.o 
	gcc main.o sum.o diff.o square.o product.o division.o unity.o -o a.out

run : all 
	./a.out

clean :
	rm -rf *.o *.out