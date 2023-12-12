#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

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
int getNodeCount(node_t *);
int getOperation(void);
int deleteFromList(void);
void addToList(void);
void printList(void);
node_t *create(void);
void insertToEnd(void);
void insertToFront(void);
void insertToList(void);
void addValue(int *);
void getInsertionPos(int *);

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

void addToList(){
  _Bool repeat_prompt = false; 
  int index = 0; 
  /* Current length of linked list */
  int len_list = getNodeCount(head);
  
  do{ 
    getInsertionPos(&index);
    
    if(index == 1){
      insertToFront();
      break;
    }
    else if(index == len_list  + 1){
      insertToEnd();
      break;
    }
    else if (index > 1 && index < len_list + 1){
      node_t *new_node = create();
      addValue(&new_node->value);

      /* Navigate to the node before the 
       * insertion position */
      current = head;
      for(int i = 1; i < index - 1; i++){
        current = current->next; 
      }

      /* Found the node before 
       * the insertion position */
      new_node->next = current->next; 
      current->next = new_node; 

      break;
    }
    else{
      printf("Cannot enter a new node at position %d. Please try again.\n", index);
      repeat_prompt = true;
    }
  }while(repeat_prompt);
}

void printList(){
  /* Is the linked list empty? */ 
  if(head == NULL){
    puts("The list is empty, nothing to display!");
    return;
  }
  int count = 1; 
  current = head; // Start from the beginning 
  while(current != NULL){
    printf("Item %d: %d\n", count, current->value);
    current = current->next; 
    count++; 
  }
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
  }
  /* Add value to the new node */
  addValue(&current->value); 
  current->next = NULL; // No more nodes                    
}

void insertToFront(){
  node_t *new_node = create();

  /* Add value to the new node */
  addValue(&new_node->value);
  /* Node after the new node is 
   * the old head node */
  new_node->next = head; 
  head = new_node; // New node is the new head node
}

void clearIOStream(void){
  /* Delete excess input characters 
   * from the input stream */
  while(getchar() != '\n')
    ;
}

void addValue(int *val){
  /* Populate the node with a value */
  printf("Type the node value: ");
  scanf("%d", val);
  clearIOStream();
}

void getInsertionPos(int *pos){
  printf("Please enter the new node position (1 to %d): ", getNodeCount(head) + 1);
  scanf("%d", pos);
  clearIOStream();
}

node_t *create(void){
  node_t *new_node = (node_t *) malloc(sizeof(node_t) * 1);

  if(new_node == NULL){
    puts("Unable to allocate memory. malloc() error.");
    exit(1); 
  }

  return(new_node);
}

int getNodeCount(node_t *head_node){
  /* Base case for recursion termination */
  if(head_node == NULL){
    return 0;
  }
  
  /* Count this current node (+1) and rest 
   * of the linked list */
  return(1 + getNodeCount(head_node->next));
}
