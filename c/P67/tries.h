// Declares a node struct

#ifndef TRIES_H
#define TRIES_H


typedef struct node {
    int nodevalue;
    int upvalue; // value till the top of the trie 
    struct node *exit[3]; // left(0) right(1) and route(2) to efficient one 
} node;

#endif // TRIES.H
