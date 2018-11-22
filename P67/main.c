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

int getnum(FILE* handler){
    char c;
    int num;
    c = fgetc(handler);
    // this breaks down if numbers are three digits.
    //
    num =  c%'0' * 10 + (c = fgetc(handler))%'0';
    num = 100 - num;
    c = fgetc(handler);

    return num;
}

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
    int num,rownum, index; // index = i for ith num of a row
    char c;
    rownum = 0;
    node *update, *start; // this is temporary storage for a node while updating the lastrow[]

    // root of the tries
    start = create();
    lastrow[0] =start;
    start->weight = getnum(handler);

    while (rownum<99){
        rownum++;
        index = -1;
        while( index < rownum ){
            index++;
            
            // prepare node to load the new number
            newnode = create();
            if (!newnode)
                return -1;
            newnode->weight = getnum(handler);
            newnode->pathup = NULL;
            newnode->left = NULL;
            newnode->right = NULL;

            // link to upper row 
            if (index == 0){
                lastrow[0]->left = newnode;
            }else if (index == rownum) {
                lastrow[index-1]->right = newnode;
            } else {
                lastrow[index-1]->right = newnode;
                lastrow[index]->left = newnode;
            }
            if (index != 0){
                lastrow[index-1] = update;  // update is the previous node in the row
            }
            update = newnode;
        }
        lastrow[index] = update;
    }
    // check this.
    return 0;
}
