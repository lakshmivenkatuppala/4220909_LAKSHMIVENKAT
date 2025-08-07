object.o : main.c sum.c diff.c square.c product.c division.c
	gcc main.c sum.c diff.c square.c product.c division.c -c

all : main.o sum.o diff.o square.o product.o division.o 
	gcc main.o sum.o diff.o square.o product.o division.o -o a.out

run : all 
	./a.out

clean :
	rm -rf *.o *.out