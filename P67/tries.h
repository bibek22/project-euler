// Declares a dictionary's functionality

#ifndef TRIES_H
#define TRIES_H


typedef struct node {
    int weight;
    struct node *pathup;
    struct node *left;
    struct node *right;
} node;

#endif // DICTIONARY_H
