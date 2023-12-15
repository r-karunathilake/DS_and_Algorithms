/* 
 * This is a command line program created to interact with a custom 
 * implementation of a binary data structure in the C programming 
 * language. The program is written and tested on Ubuntu.
 *
 *   Ubuntu version: 22.04.3 LTS
 *   C/C++ compiler version: CLang 14.0.0-1ubuntu1.1 
 *   Linux kernel version: 5.15.90.1-microsoft-standard-WSL2
 *
 * Author: Ravindu Karunathilake
 * Date:   2023/12/15
 *
 * */

/* Tree node definition */ 
typedef struct node{
  int data;
  struct node *left;
  struct node *right;
} node_t;

/* TODOs: 
 *  Basic operations of a binary tree:
 *    - Inserting a node
 *    - Removing a node 
 *    - Searching for a node
 *    - Find the height of the tree 
 *    - Find the levels of the tree
 *    - Find the Size of the entire tree 
 * */

