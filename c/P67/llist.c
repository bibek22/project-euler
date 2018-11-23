#include <stdio.h> 
#include "llist.h"
#include "tries.h"

llist *createlist(){
    // instantiates a linked list node with NULL vlaues
    llist *newllist = malloc(sizeof(llist));
    if (!newllist){
        fprintf(stderr, "couldn't allocate memory.");
        return NULL;
    }else {
        newllist->this = NULL;
        newllist->next = NULL;
        return newllist;
    }
}

int search(llist *target, node* node){
    // returns 1 if the data is found, 0 otherwise
    int found = 0;
    while (( target->this != node ) && (target->next != NULL)){
        target = target->next;
    }
    if (target->this == node){
        found = 1;
    }
    return found;
}

int delete(llist *target, node* node){
    llist *prior = NULL;
    while (( target->this != node ) && (target->next != NULL)){
        prior = target;
        target = target->next;
    }
    if (target->this == node){
        llist *next = target->next;
        free(target);
        prior->next = next;
        return 0;
    }else if (target->next == NULL){
        return 1;
    }
}

void demolish(llist *target){
    //frees up the heap memory used by the linked list.
    if (target->next == NULL){
        free(target);
    }
    demolish(target->next);
    free(target);
}
