#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "tries.h"
#include "tries.c"

typedef struct llist {
    struct llist* prev;
    struct llist* next;
    node *this;
} llist;

int main(int argc, char *argv[]){
    node *lastrow[100], *newnode;
    for (int i = 0; i <100; i++){
        lastrow[i] = NULL;
    }

    if (argc != 2){
        fprintf(stderr, "Usage: main <filename>");
        return 1;
    }
    FILE *handler = fopen(argv[1], "r");
    int num, index; // index = i for ith num of a row
    char c;
    index = 0;
    node *update, *start; // this is temporary storage for a node while updating the lastrow[]
    start = NULL;
    while ( c != EOF ){
        index++;
        if (c == '\n'){
            index = 0;  // new row begins
        }
        if (isdigit( (c=fgetc(handler) ))){
            // this breaks down if numbers are three digits.
            num =  c%'0' *10 + (c = fgetc(handler))%'0';
            num = 100 - num;
            printf("adding %d\n", num);

            // prepare node to load the new number
            newnode = create();
            if (! start){
                start = newnode;
            }
            newnode->weight = num;
            newnode->left = lastrow[index];
            newnode->right = lastrow[index+1];
            newnode->pathup = NULL;

            // update lastrow
            if (index > 0){
                lastrow[index-1] = update;
            }
            update = newnode;
        }
        // check this.
        lastrow[index-1] = update;
        c = fgetc(handler);
    }
    destroy(start);
    return 0;
}

void dijkstra(node *start){



}

void compete(llist* lboard, llist* competer){
    while (lboard->this->weight < competer->this->weight){
        if (! lboard->next){
            lboard->next = competer;
        }
        lboard = lboard->next;
    }
}

void cliptail(llist *lboard){
    if (lboard){ 
        cliptail(lboard->next);
    }
    free(lboard);
}
