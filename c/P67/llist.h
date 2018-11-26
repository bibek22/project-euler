#ifndef LLIST_H
#define LLIST_H

#include "tries.h"

typedef struct llist {
   node* this; 
   struct llist* next;

} llist;

llist* createlist(void);
int search(llist *target, node *node);
int delete(llist *target, node *node);
void demolish(llist *target);


#endif // LLIST_H
