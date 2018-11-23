#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "tries.h"
#include "tries.c"
#define LEFT 0
#define RIGHT 1
#define PATHUP 1

typedef struct llist {
    struct llist* prev;
    struct llist* next;
    node *this;
} llist;

void resolveNode(node *start){
    // do the arithmetic and optimization at the node and update the pathup
    node* child;
    for (int i = 0;i<2;i++){
    child = start->exit[i];
    if (child->exit[PATHUP] == NULL){
        child->upvalue += start->upvalue;
        child->exit[PATHUP] = start;
    }else if ( child->upvalue > start->upvalue + child->nodevalue ){
        child->upvalue = start->upvalue + child->nodevalue;
        child->exit[PATHUP] = start;
    }
    }


}

void dijkstra(node *start){
    // to be implemented.
    resolveNode(start);
    

}

void compete(llist* lboard, llist* competer){
    // this is for when implementing dijkstra algo, a linked list of 
    // nodes that have minimum value.
    while (lboard->this->upvalue < competer->this->upvalue){
        if (! lboard->next){
            lboard->next = competer;
        }
        lboard = lboard->next;
    }
}

void cliptail(llist *lboard){
    // if i ever wanted to clip a linked list 
    // to free some memory
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

    // root of the trie 
    start = create();
    lastrow[0] =start;
    start->nodevalue = getnum(handler);

    while (rownum<99){
        // populate all 100 rows of nodes
        rownum++;
        index = -1;
        while( index < rownum ){
            index++;
            
            // prepare node to load the new number
            newnode = create();
            if (!newnode)
                return -1;
            newnode->nodevalue = getnum(handler);
            newnode->exit[PATHUP] = NULL;
            newnode->exit[LEFT] = NULL;
            newnode->exit[RIGHT] = NULL;

            // link to upper row 
            if (index == 0){
                lastrow[0]->exit[LEFT] = newnode;
            }else if (index == rownum) {
                lastrow[index-1]->exit[RIGHT] = newnode;
            } else {
                lastrow[index-1]->exit[RIGHT] = newnode;
                lastrow[index]->exit[LEFT] = newnode;
            }
            if (index != 0){
                lastrow[index-1] = update;  // update is the previous node in the current row
            }
            update = newnode;
        }
        lastrow[index] = update;
    }
    return 0;
}
