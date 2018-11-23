#include <stdlib.h>
#include <stdio.h>
#include "tries.h"

void destroy(node* table){
    // to free all the heaps memory 
    node* next[2];
    next[0] = table->left;
    next[1] = table->right;

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
        dict->right = new;
    else
        dict->left = new;

    new->left = NULL;
    new->right = NULL;
    return new;
}

node* create(){
    node* table = NULL;
    table = malloc(sizeof(node));
    table->left = NULL;
    table->right = NULL;
    return table;
}

