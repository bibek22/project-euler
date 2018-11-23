#include <stdlib.h>
#include <stdio.h>
#include "tries.h"
#define LEFT 0
#define RIGHT 1
#define PATHUP 2

void destroy(node* table){
    // to free all the heaps memory 
    node* next[2];
    next[0] = table->exit[LEFT];
    next[1] = table->exit[RIGHT];

    for (int i=0; i < 2; i++){
        node* nextnode;
        nextnode = next[i];
        if (nextnode != NULL){
            destroy(next[i]);
        }
        free(nextnode);
    }
}

node* add(node *dict, int toright){
    node *new = NULL;
    new = malloc(sizeof(node));
    if (!new){
        fprintf(stderr, "Unable to alocate memory.");
        return NULL;
    }
    if (toright)
        dict->exit[RIGHT] = new;
    else
        dict->exit[LEFT] = new;

    new->exit[LEFT] = NULL;
    new->exit[RIGHT] = NULL;
    return new;
}

node* create(){
    node* table = NULL;
    table = malloc(sizeof(node));
    table->exit[LEFT] = NULL;
    table->exit[RIGHT] = NULL;
    return table;
}

