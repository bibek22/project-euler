#include <stdio.h>
#include <stdlib.h>
#include "tries.h"
#include "llist.h"

llist* compete(llist* lboard, node* competer){
    // when implementing dijkstra algo, maintains a l(eader)board.
    // takes a linked list of leaderboard and a trie node  
    llist *newEntry, *lastCompared;
    llist* lboardBackup;
    lboardBackup = lboard;
    newEntry = createlist();
    newEntry->this = competer;
    lastCompared = lboard;
    while (lboard->this->upvalue < newEntry->this->upvalue){
        printf("lbvalue = %d\n", lboard->this->nodevalue);
        if (! lboard->next){
            // if reached the end of the leaderboard
            lboard->next = newEntry;
            return lboardBackup;
        }else 
            lastCompared = lboard;
            lboard = lboard->next;
    }
    // at this point:
    // lboard == the node with node having just greater upvalue than our competer
    // so insert newnode just before it.
     
    lastCompared->next = newEntry;
    newEntry->next = lboard;
    return newEntry;
}

llist* resolveNode(llist* lboard, node *nodeToSolve){
    // do the arithmetic and optimization at the node and update the pathup
    node* child;
    for (int i = 0;i<2;i++){  // left and right child
        child = nodeToSolve->exit[i];
        if (child->exit[PATHUP] == NULL){
            child->upvalue = nodeToSolve->upvalue + child->nodevalue;
            child->exit[PATHUP] = nodeToSolve;
        }else if ( child->upvalue > nodeToSolve->upvalue + child->nodevalue ){
            child->upvalue = nodeToSolve->upvalue + child->nodevalue;
            child->exit[PATHUP] = nodeToSolve;
        }
        lboard = compete(lboard, child);
    }
    // now the node at nodeToSolve is done. remove it from lboard.
    printf("%d is done\n", lboard->this->nodevalue);
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
    if (lboard->next){ 
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
    node *update, *start, *startbackup; // this is temporary storage for a node while updating the lastrow[]

    // root of the trie 
    start = create();
    startbackup = start; // for when freeing at last.
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
            newnode->upvalue = 10000;
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
    // main() above this works as intended
    start = dijkstra(start);
    //start now is the node at the bottom row of trie
    printf("The minimal value of %d", 10000-start->upvalue);
    destroy(startbackup);
    return 0;
}
