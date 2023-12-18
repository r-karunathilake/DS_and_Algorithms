/* 
 * This is a command line program created to interact with a custom 
 * implementation of a binary data structure in the C programming 
 * language. The program is written and tested on Ubuntu.
 *
 *   Ubuntu version: 22.04.3 LTS
 *   
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
#include <string.h>

/* Tree node definition */ 
typedef struct node{
  int data;
  struct node *left;
  struct node *right;
} node_t;

/* Function prototypes */
node_t *createNode(void);
void getData(int *);
void clearIOStream(void);
void printTree(void);
void printPreOrder(node_t *);
void printInOrder(node_t *);
void printPostOrder(node_t *);
void printLevelOrder(node_t *);
void addNode(node_t *, node_t *);
int getOperation(void);

/* Global variables */
node_t *root = NULL;

/* TODOs: 
 *  Basic operations of a binary tree:
 *    - Inserting a node
 *    - Removing a node 
 *    - Searching for a node
 *    - Find the height of the tree 
 *    - Find the levels of the tree
 *    - Find the Size of the entire tree 
 * */

int main(int argc, char *argv[]){
  int operation = '\0';
  while(operation != 'Q'){
    operation = getOperation();
    
    switch(operation){
      case 'S':{
        printTree();
        // This should print the height
        // number of levels, and size of the entire tree. 
      }break;
      
      case 'A':{
        addNode(createNode(), root);
      }break;

      case 'R':{
        //removeNode();
      }break;

      case 'Q':{
        /* Quit the while-loop and exit main() */
      }break;

      default:{
        printf("Invalid operation: %c. Please enter a valid operation!", operation);
      }
    }
  }
  return(0);
}

void printTree(){
  char order[3];
  printf("Print order Pr)e order, In)-order, Po)st-order, Le)vel-order: ");
  fgets(order, 3, stdin);
  clearIOStream();
  
  /* Convert string to uppercase */
  int index = 0;
  while(order[index]){
    int ch = order[index];
    if(islower(ch)){
      order[index] = toupper(ch);
    }
    index++;
  }

  if(strcmp(order, "PR") == 0){
    printPreOrder(root);
    putchar('\n');
  }
  else if(strcmp(order, "IN") == 0){
    //printInOrder();
  }
  else if(strcmp(order, "PO") == 0){
    //printPostOrder();
  }
  else if(strcmp(order, "LE") == 0){
    //printLevelOrder();
  }
  else{
    puts("Error: invalid print order!");
  }
}

void addNode(node_t *new_node, node_t *current){
  /* TODO: Make sure the node are ordered as its
   * entered into the tree */

  /* Tree is empty? */ 
  if(current == NULL){
    root = new_node;
    return; 
  }

  /* Insert left */
  if(new_node->data <= current->data){
    /* Left recursive base case */
    if(current->left == NULL){
      current->left = new_node;
    }
    else{
      addNode(new_node, current->left);
    }
  }
  /* Insert right */
  else{
    /* Right recursive base case */
    if(current->right == NULL){
      current->right = new_node;
    }
    else{
      addNode(new_node, current->right);
    }
  }
}

void printPreOrder(node_t *current){
  /* Recursive base case */ 
  if(current == NULL){
    return;
  }

  /* Display head node for each level */
  printf("%d ", current->data);

  /* Left child node first */ 
  if(current->left != NULL){
    printPreOrder(current->left);
  }

  /* Right child node second */ 
  if(current->right != NULL){
    printPreOrder(current->right);
  }
}

node_t *createNode(void){
  node_t *new_node = (node_t *) malloc(sizeof(node_t) * 1);

  if(new_node == NULL){
    puts("Error: unable to allocate memory for tree node!");
    exit(1);
  }

  /* Initialize the new node */
  getData(&new_node->data);
  
  /* NULL pointer for left and right nodes */ 
  new_node->left = NULL;
  new_node->right = NULL;

  return(new_node);
}

void getData(int *val){
  printf("Enter an integer value for the node data: ");
  scanf("%d", val);
  clearIOStream();
}

int getOperation(void){
  printf("S)how the tree, A)dd to the tree, R)emove from tree, Q)uit: ");
  int choice = toupper(getchar());
  clearIOStream();

  return(choice);
}

void clearIOStream(void){
  /* Delete excess input characters 
   * from the input stream */
  while(getchar() != '\n')
    ;
}
