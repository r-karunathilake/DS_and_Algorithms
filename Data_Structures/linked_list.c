/* 
 * This is a command line program created to interact with a custom 
 * implementation of a linked list data structure in the C programming 
 * language. The program is written and tested on Ubuntu. The user is able 
 * to display, add, and deletes notes from the linked list. 
 *
 *   Ubuntu version: 22.04.3 LTS
 *   C/C++ compiler version: CLang 14.0.0-1ubuntu1.1 
 *   Linux kernel version: 5.15.90.1-microsoft-standard-WSL2
 *
 * Author: Ravindu Karunathilake
 * Date:   2023/12/15
 *
 * */

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
void deleteFromList(void);
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

int getOperation(void){
  printf("S)how the list, A)dd to the list, R)emove from list, Q)uit: ");
  int choice = toupper(getchar());
  clearIOStream();

  return(choice);
}

void addToList(void){
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
      printf("Cannot enter a new item at position %d. Please try again.\n", index);
      repeat_prompt = true;
    }
  }while(repeat_prompt);
}

void deleteFromList(void){
  /* Is the linked list empty? */
  if(head == NULL){
    puts("No items to delete!");
    return; 
  }
  
  int del_pos = 0;
  puts("Choose item to delete: ");
  printList();
  printf("Item: ");
  scanf("%d", &del_pos);
  clearIOStream();

  /* Check for invalid user input <= 0 */
  if(del_pos <= 0){
    printf("Invalid item position %d", del_pos);
    return; 
  }

  current = head;
  node_t *prev_node = NULL;
  /* Go to the node to be deleted */
  for(int i = 1; i < del_pos; i++){
    /* 'current' is the node prior
     * to the node to be deleted */
    prev_node = current;
    
    /* 'current' is the node to be deleted */
    current = current->next;
    
    if(current == NULL){
      printf("Specified item number %d not found!", del_pos);
      return;
    }
  }
  
  /* Deleting the first node in the linked list */
  if(prev_node == NULL){
    head = current->next;
  }
  else{
    prev_node->next = current->next;
  }

  /* Release memory for the current item */ 
  free(current);
  printf("Item %d removed successfully!\n", del_pos); 
}

void printList(void){
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

void insertToEnd(void){
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

void insertToFront(void){
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
  printf("Please enter the new item position (1 to %d): ", getNodeCount(head) + 1);
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
