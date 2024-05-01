/* 
 * This is a hash table implementation written in the C programming
 * language. The user is able to search, insert and delete key-value 
 * pairs from the hash table. 
 *
 *   Ubuntu version: 22.04.3 LTS
 *   C/C++ compiler version: CLang 14.0.0-1ubuntu1.1 
 *   Linux kernel version: 5.15.90.1-microsoft-standard-WSL2
 *
 * Author: Ravindu Karunathilake
 * Date:   2024/01/03
 *
 * */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* Randomly picked prime numbers for double 
 * hashing purposes */ 
#define PRIME_1 1093 
#define PRIME_2 2029

/* Base size of the hash table */
#define INITIAL_SIZE 50

/* Table resizing load factors */
#define SIZE_UP_FACTOR   0.7
#define SIZE_DOWN_FACTOR 0.1

/* Hash table key-value pair */
typedef struct {
  char* key;
  char* value;
} item_pair; 

/* global sentinel item representing
 * a deleted item */ 
static item_pair DELETED_ITEM = {NULL, NULL};

/* Hash table */
typedef struct{
  int base_size; 
  int size;
  int count;
  item_pair** items; // An array of pointer to items  
} hash_table; 

/* Function prototypes */
static item_pair* create_item(const char* key, const char* value);
hash_table* init_hash_table();
static void delete_item(item_pair* item);
void delete_table(hash_table* table); 
static int hash(const char* string, const int prime, const int table_size);
void insert(hash_table* table, const char* key, const char* value);
char* search(hash_table* table, const char* key);
void entry_del(hash_table* table, const char* key);
static void table_resize_up(hash_table* table);
static void table_resize_down(hash_table* table);
static hash_table* resized_table(const int base_size);
