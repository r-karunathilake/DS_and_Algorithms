#include <stdio.h>
#include <stdlib.h>

/* Linked list node definition */
typedef struct node{
  int value;
  struct node *next;
}node_t;

/* Global variables */ 
node_t *head = NULL;
node_t *current;

/* Function prototypes */ 
void clearIOStream(void);
int getOperation(void);

int main(int argc, char *argv[]){
  int operation = '\0';

  while(operation != 'Q'){
    operation = getOperation();
    switch(operation){
    
      default:{
        printf("Invalid operation: %c. Please enter a valid operation!", operation);
      }
    }
  }
  return(0);
}

int getOperation(){
  printf("S)how the list, A)dd to the list, R)emove from list, Q)uit: ");
  int choice = toupper(getchar());

  if(choice == 'A'){
    printf("Add to the E)nd or B)eginning of the list: ");
    choice = toupper(getchar());
    clearIOStream();
  }

  return(choice);
}

void clearIOStream(void){
  /* Delete excess input characters 
   * from the input stream */
  while(getchar() != '\n')
    ;
}


