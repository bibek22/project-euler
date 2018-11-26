

# target: dependencies
# 	action

main: main.o tries.o llist.o
	gcc main.o tries.o llist.o -o main

main.o: main.c
	gcc -c main.c

tries.o: tries.c
	gcc -c tries.c

llist.o: llist.c
	gcc -c llist.c

clean:
	rm *.o main

