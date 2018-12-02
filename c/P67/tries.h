// Declares a node struct

#ifndef TRIES_H
#define TRIES_H

#define LEFT 0
#define RIGHT 1
#define PATHUP 2

typedef struct node {
    int nodevalue;
    int upvalue; // value till the top of the trie 
    struct node *exit[3]; // left(0) right(1) and route(2) to efficient one 
} node;

int destroy(node* table, int hitend);
node* add(node *dict, int toright);
node* create(void);


#endif // TRIES.H
