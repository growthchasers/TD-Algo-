#include <stdio.h>

int main() {
    double s = 1; 

    for (int i = 10; i <= 20; i++) {
        s += 1.0 / i;   
    }

    printf("S = %.6f\n", s); 
    return 0;
}
