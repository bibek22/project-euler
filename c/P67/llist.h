#ifndef LLIST_H
#define LLIST_H

#include <stdio.h>
#include <stdlib.h>
#include "tries.h"

typedef struct llist {
   node* this; 
   struct llist* prev;
   struct llist* next;

} llist;


#endif // LLIST_H
