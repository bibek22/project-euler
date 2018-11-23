#include <stdio.h>
#include <stdlib.h>
#include "tries.h"
#include "llist.h"
#include "llist.c"
#include "tries.c"

llist* compete(llist* lboard, node* competer){
    // this is for when implementing dijkstra algo, maintains a l(eader)board.
    // takes a linked list of leaderboard and a llist node  
    llist* newnode;
    newnode = createlist();
    newnode->this = competer;
    while (lboard->this->upvalue < newnode->this->upvalue){
        printf("On compete.\n");
        printf("nodevalue = %d\n", newnode->this->nodevalue);
        printf("lbvalue = %d\n", lboard->this->nodevalue);
        if (! lboard->next){
            // if reached the end of the leaderboard
            lboard->next = newnode;
            break;
        }else 
            lboard = lboard->next;
    }
    // at this point:
    // lboard == the node with node having just greater upvalue than our competer
    // so insert newnode just before it.
    
    newnode->next = lboard;
    return newnode;
}

llist* resolveNode(llist* lboard, node *start){
    // do the arithmetic and optimization at the node and update the pathup
    node* child;
    for (int i = 0;i<2;i++){  // left and right child
        child = start->exit[i];
        if (child->exit[PATHUP] == NULL){
            child->upvalue = start->upvalue + child->nodevalue;
            child->exit[PATHUP] = start;
        }else if ( child->upvalue > start->upvalue + child->nodevalue ){
            child->upvalue = start->upvalue + child->nodevalue;
            child->exit[PATHUP] = start;
        }
        lboard = compete(lboard, child);
    }
    // now the node at start is done. remove it from lboard.
    llist* tmp;
    tmp = lboard;
    lboard = lboard->next;
    free(tmp);
    return lboard;
}

node* dijkstra(node *start){
    // to be implemented.
    llist* lboard = NULL;
    lboard = createlist();
    lboard->this = start;
    while(1){  // till reached the end of the leaderboard(?)
        printf("Doing\n");
        lboard = resolveNode(lboard, start);
        start = lboard->this;
        if ((start->exit[LEFT] == NULL) && (start->exit[RIGHT] == NULL)){
            break; 
            //you're at the bottom of the triangle. and this algo implies backtracing
            // start gives you the optimal path.
        }
    }

    demolish(lboard);
    return(start);
}

void cliptail(llist *lboard){
    // if i ever wanted to clip the tail off a linked list 
    // to free some memory
    if (lboard){ 
        cliptail(lboard->next);
    }
    free(lboard);
}

int getnum(FILE* handler){
    char c;
    int num;
    c = fgetc(handler);
    // this breaks down if numbers are three digits.
    //
    num =  c%'0' * 10 + (c = fgetc(handler))%'0';
    num = 100 - num;
    c = fgetc(handler);

    return num;
}

int main(int argc, char *argv[]){
    node *lastrow[100], *newnode;
    for (int i = 0; i <100; i++){
        lastrow[i] = NULL;
    }

    if (argc != 2){
        fprintf(stderr, "Usage: main <filename>");
        return 1;
    }

    FILE *handler = fopen(argv[1], "r");
    int num,rownum, index; // index = i for ith num of a row
    char c;
    rownum = 0;
    node *update, *start; // this is temporary storage for a node while updating the lastrow[]

    // root of the trie 
    start = create();
    lastrow[0] =start;
    start->nodevalue = getnum(handler);
    start->upvalue = start->nodevalue;

    while (rownum<99){
        // populate all 100 rows of nodes
        rownum++;
        index = -1;
        while( index < rownum ){
            index++;
            
            // prepare node to load the new number
            newnode = create();
            if (!newnode)
                return -1;
            newnode->nodevalue = getnum(handler);
            newnode->exit[PATHUP] = NULL;
            newnode->exit[LEFT] = NULL;
            newnode->exit[RIGHT] = NULL;

            // link to upper row 
            if (index == 0){
                lastrow[0]->exit[LEFT] = newnode;
            }else if (index == rownum) {
                lastrow[index-1]->exit[RIGHT] = newnode;
            } else {
                lastrow[index-1]->exit[RIGHT] = newnode;
                lastrow[index]->exit[LEFT] = newnode;
            }
            if (index != 0){
                lastrow[index-1] = update;  // update is the previous node in the current row
            }
            update = newnode;
        }
        lastrow[index] = update;
    }
    // delete the array if possible

    start = dijkstra(start);
    //start now is the node at the bottom row of trie with pathup leading to optimal path
    //but path is not what we need right now. 
    printf("The minimal value of %d", 10000-start->upvalue);
    return 0;
}
