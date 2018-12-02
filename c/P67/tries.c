#include <stdlib.h>
#include <stdio.h>
#include "tries.h"

int destroy(node* root, int hitend){
    node* next[2];
    next[1] = root->exit[RIGHT];
    next[0] = root->exit[LEFT];

    for (int i=0; i < 2; i++){
        if (hitend && (i ==1))
            return hitend;
        if (next[i])
            hitend = destroy(next[i], hitend);
        else
            hitend = 1;
    }
    free(root);
    return hitend;
}

node* add(node *dict, int index){
    node *new = NULL;
    new = malloc(sizeof(node));
    if (!new){
        fprintf(stderr, "Unable to alocate memory.");
        return NULL;
    }
    if (index==RIGHT)
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

