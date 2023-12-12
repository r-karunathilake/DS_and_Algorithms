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
node_t *create(void);
void insertToEnd(void);

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
        //deleteFromList();
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
        insertToEnd(); // TODO: fix fcn arguments 
      }break;

      case 'B':{
        //insertToFront(); // TODO: fix fcn arguments
      }break;

      case 'M':{         
        //insertToList(); // TODO: fix fcn arguments 
      }break;
      
      default:{
        choice = 'R'; 
      }
    }
  }while(choice == 'R'); // Repeat prompt
}

void insertToEnd(){
  /* Empty linked list? */
  if(head == NULL){
    head = create();
    current = head; 
  }
  else{
    current = head;

    /* Traverse the linked list and find the 
     * NULL pointer (end of the linked list) */
    while(current->next != NULL){
      current = current->next; // Go to the next node
    }    

    /* Reached the end of the linked list */
    current->next = create();
    current = current->next; // Points to last node

    /* Populate the last node with a value */
    printf("Type the value to append: ");
    scanf("%d", &current->value);
    current->next = NULL; // No more nodes
                    
    clearIOStream();      
  }
}

void clearIOStream(void){
  /* Delete excess input characters 
   * from the input stream */
  while(getchar() != '\n')
    ;
}

node_t *create(void){
  node_t *new_node = (node_t *) malloc(sizeof(node_t) * 1);

  if(new_node == NULL){
    puts("Unable to allocate memory. malloc() error.");
    exit(1); 
  }

  return(new_node);
}
