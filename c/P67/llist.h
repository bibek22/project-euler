#include <stdio.h>
#include <stdlib.h>
#include "tries.h"

typedef struct llist {
   node* this; 
   struct llist* prev;
   struct llist* next;

} llist;
