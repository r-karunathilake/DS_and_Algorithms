#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

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
int deleteFromList(void);
void addToList(void);
void printList(void);

int main(int argc, char *argv[]){
  int operation = '\0';

  while(operation != 'Q'){
    operation = getOperation();
    switch(operation){
      case 'S': {
        printList();  
      }break;

      case 'A': {
        addToList();
      }break;

      case 'R': {
        deleteFromList();
      }break;

      case 'Q': {
        /* Quit the while-loop and exit main() */
      }break;

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
  clearIOStream();

  return(choice);
}

void printList(){
 /* Is the linked list empty? */ 
  if(head == NULL){
    puts("The list is empty, nothing to display!");
    return;
  }
  int count = 1; 
  while(current != NULL){
    printf("Item %d: %d\n", count, current->value);
    current = current->next; 
    count++; 
  }
}

void addToList(){
  printf("Add to the E)nd , B)eginning or M)iddle of the list: ");
  int choice = toupper(getchar());
  clearIOStream();
  do{
    switch(choice){
      case 'E':{  
        addToEnd(); // TODO: fix fcn arguments 
      }break;

      case 'B':{
        addToFront(); // TODO: fix fcn arguments
      }break;

      case 'M':{         
        insertToList(); // TODO: fix fcn arguments 
      }break;
      
      default:{
        choice = 'R'; 
      }
    }
  }while(choice == 'R'); // Repeat prompt
}

void clearIOStream(void){
  /* Delete excess input characters 
   * from the input stream */
  while(getchar() != '\n')
    ;
}


