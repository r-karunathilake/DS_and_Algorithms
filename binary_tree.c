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
#include <stdbool.h>

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
node_t *removeNode(node_t *, int);
_Bool contains(node_t *, int);
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
        int rm_val;
        printf("Which value do you want to delete: ");
        scanf("%d", &rm_val);
        clearIOStream();

        root = removeNode(root, rm_val);
      }break;

      case 'C':{
        int val; 
        printf("Value to check: ");
        scanf("%d", &val);
        clearIOStream();

        if(contains(root, val)){
          printf("The requested value %d is in the tree\n", val);
        }
        else{
          printf("The requested value %d is NOT in the tree\n", val);
        }
      }break;

      case 'Q':{
        /* Quit the while-loop and exit main() */
      }break;

      default:{
        printf("Invalid operation: %c. Please enter a valid operation!\n", operation);
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

node_t *removeNode(node_t *head, int val){
  /* Is the tree empty? */
  if(root == NULL){
    puts("Tree is empty. Nothing to remove");
    return root;
  }
  
  /* Recursive base case */
  if(head == NULL){
    return head;
  }

  /* Navigate the tree and find the 
   * value to be deleted */
  if(val < head->data){
    head->left = removeNode(head->left, val);
    return head;
  }
  else if(val > head->data){
    head->right = removeNode(head->right, val);
    return head; 
  }

  /* We have found the node to be deleted */
  
  /* If one child is empty */ 
  if(head->left == NULL && head->right != NULL){
    node_t *temp = head->right;
    free(head);
    return temp; // Child node is now the new head
  }
  else if(head->right == NULL && head->left != NULL){
    node_t *temp = head->left;
    free(head);
    return temp; // Child node is now the new head
  }
  /* Both children exist */
  else{
    /* Find the leaf node used for replacement */ 

    /* Assume the current node is the parent to a
     * leaf node */ 
    node_t *leaf_parent = head;

    /* Assume the right child is the leaf node*/
    node_t *leaf_node = head->right;

    /* Verify the leaf node assumptions */ 
    while(leaf_node->left != NULL){ // Assumption is not correct
      /* Keep going down the tree */ 
      leaf_parent = leaf_node;
      leaf_node = leaf_node->left; 
    }

    if(leaf_parent != head){
      /* Save the leaf nodes right branch to parent */
      leaf_parent->left = leaf_node->right;
    }
    else{
      leaf_parent->right = leaf_node->right;
    }

    head->data = leaf_node->data;

    free(leaf_node);
    return head; 
  }
}

_Bool contains(node_t *current, int value){
  /* Is the tree empty? */ 
  if(current == NULL){
    return false;
  }

  /* Recursive base case */ 
  if(value == current->data){
    return true;
  }

  /* Check left */
  else if(value < current->data){
    if(current->left == NULL){
      return false; 
    }
    else{
       return contains(current->left, value);
    }
  }

  /* Check right */
  else{
    if(current->right == NULL){
      return false;
    }
    else{
      return contains(current->right, value);
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
  printf("S)how the tree, A)dd to the tree, R)emove from tree, C)heck value, Q)uit: ");
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
