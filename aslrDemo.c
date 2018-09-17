// A few versions of a C program I worte, playing with formatting, trying to demonstrate ASLR
// A good way to check against a binary is with the command,'ldd <PE> | grep libc'


// Description by line

// Signal prepocessor with # to include standard i/o header file for printf function
// main() is normally the starting function. int indicates main accepts an integer for status of program termination. void, to mean the function doesn't accept paramaters 
// register asks the compiler to put the var in a CPU register instead of RAM. int for integer initialization, i for var name, asm for assembler instruction and esp the named instruction location
// printf function, like echo or push to std ut.  esp for our asm var. % for replace with var i. # for 0x, 8 for 8 chars, x for unsigned hex formatting. \n newline.  i is integer


/*
#include <stdio.h>
void main() {
	register int i asm("esp");
	printf("$esp = %#10x\n", i);
}






#include <stdio.h>
void main() {
    register int i asm("esp");
	printf("$esp = %8x\n", i);
}





#include <stdio.h>
void main() {
	register int i asm("esp");
	printf("$esp = %x8x\n", i);
}





#include <stdio.h>
int main(void) {
	register int i asm("esp");
	printf("$esp = %#8\n", i);
}





#include<stdio.h> 
int main(void) {  
	register int i asm("esp"); 
	printf("$esp = %#8x\n", i); 
}

*/




#include <stdio.h>
void main() {
	register int i asm("esp");
	printf("$esp = %#010x\n", i); 
}
