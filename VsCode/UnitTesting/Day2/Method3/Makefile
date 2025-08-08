# Creating our own variable:

SRCS = main.c sum.c diff.c square.c product.c division.c
OBJS = main.o sum.o diff.o square.o product.o division.o
object.o : $(SRCS)
	gcc $^ -c

all : $(OBJS)
	gcc $^ -o $@

run : all 
	./all

clean :
	rm -rf *.o *.out all