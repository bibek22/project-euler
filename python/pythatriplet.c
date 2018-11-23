/* Author: Bibek Gautam */
/* Date: 22 Nov. 2018   */

#include <stdio.h>


int main(void){
    int maxperimeter = 1000; // according to the question
    int a, b, c, counter, maxtriplet, targetnum;  // a and b make the perpendicular pair
    int perimeter = 3;
    maxtriplet = 0;
    while (perimeter < maxperimeter){
        // this loop checks for a fix perimeter
        perimeter++;
        a = 0; 
        counter = 0;
        while (a < perimeter/2){
            // this loop checks for a fix value of a side 'a'
            a++;
            for (b = a; b < perimeter - a; b++){
                c = perimeter - a - b;
                // since c must be more than either of a and b, as it is a hypotenuse.
                if ((c < a)|| (c<b) ){
                    b = perimeter;
                    break;
                // break out if it's the case
                }
                // else check for the pythagorian condition 
                if (c*c == (a*a + b*b)){
                    counter++;
                }
            }

    
        }
        if (counter > maxtriplet){
            maxtriplet = counter;
            targetnum = perimeter;
            }       
    }
    printf("Solution maximized for %d with %d total.\n ", targetnum, maxtriplet);
    return 0;
}
