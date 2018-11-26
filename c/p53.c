#include <stdio.h>


    
int main(void){
    double factorials[101];
    int i = 1;
    double factorial = 1;
    factorials[0] = 1;

    while (i <= 100){
        factorial *= i;
        factorials[i] = factorial;
        i++;
    }

    i = 23;
    int r, total = 0;
    int broken = 0;

    while (i <= 100){
        broken = 0;
        for (r = 0; r <= i ; r++){
            factorial = factorials[i]/factorials[r]/factorials[i-r];
            if (factorial > 1000000){
                broken = 1;
                break;
            }
        } 
        if (broken)
            total += i+1 - 2*(r);
        i++;
    }
    printf("%d results.\n", total);
}
