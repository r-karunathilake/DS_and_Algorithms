#include "hash_table.h"
#include "prime.h"

static item_pair* create_item(const char* key, const char* value){
  item_pair* new_item = (item_pair*) malloc(sizeof(item_pair) * 1);
  
  if(new_item == NULL){
    fprintf(stderr, "Error: unable to allocate hash table item memory!");
    exit(1);
  }

  /* Create mutable copies of the provided strings using 
   * malloc on the heap */ 
  new_item->key = strdup(key);
  new_item->value = strdup(value);

  return new_item;
}

hash_table* init_hash_table(){
  hash_table* table = (hash_table*) malloc(sizeof(hash_table) * 1);
  
  table->base_size = INITIAL_SIZE; 
  table->size = INITIAL_SIZE;
  table->count = 0;
  table->items = (item_pair**) calloc((size_t) table->size, sizeof(item_pair*));

  if(table->items == NULL){
    fprintf(stderr, "Error: unable to allocate memory for has table!");
    exit(1);
  }

  return table; 
}

static void delete_item(item_pair* item){
  /* Mark memory for reuse */ 
  free(item->key);
  free(item->value); 
  free(item);
  
  /* Leave the memory in a well-defined state */
  item->key = NULL;
  item->value = NULL; 
}

void delete_table(hash_table* table){
  for(size_t i = 0; i < table->size; i++){
    item_pair* item = table->items[i];
    if(item != NULL){
      delete_item(item);
    }
  }

  free(table->items);
  free(table);

  /* Leave memory in a well-defined state */
  table->count = 0;
  table->base_size = 0;
  table->size = 0;
  table->items = NULL; 
}

static int hash(const char* string, const int prime, const int table_size){
  long hash = 0; 
  const int str_len = strlen(string);

  for(int i = 0; i < str_len; i++){
    hash += (long) pow(prime, str_len - (i + 1)) * string[i];
    hash %= table_size; 
  }

  return (int) hash;
}

static int get_hash(const char* string, const int size, const int attempts){
  /* Implements double hashing avoid collisions and
   * improve key-value clustering problem */ 
  const int hash_a = hash(string, PRIME_1, size);
  const int hash_b = hash(string, PRIME_2, size);

  return(hash_a + (attempts * (hash_b + 1))) % size;
}

void insert(hash_table* table, const char* key, const char* value){
  const int load = table->count / table->size;
  if(load > SIZE_UP_FACTOR){
    table_resize_up(table);
  }

  item_pair* item = create_item(key, value);
  int idx = get_hash(item->key, table->size, 0);
  item_pair* found_item = table->items[idx];

  int attempts = 1;
  /* If a collision occurs, attempt rehashing to another
   * table index */ 
  while(found_item != NULL){
    /* Possible update an item in the table */
    if(found_item != &DELETED_ITEM){
      if(strcmp(found_item->key, key) == 0){
        delete_item(found_item);
        table->items[idx] = item; // Update item
        return;
      }
    }

    /* Add a new key-value pair to the table */ 
    idx = get_hash(item->key, table->size, attempts);
    found_item = table->items[idx];
    attempts++; 
  }

  table->items[idx] = item;
  table->count++;
}

char* search(hash_table* table, const char* key){
  int idx = get_hash(key, table->size, 0);

  item_pair* item = table->items[idx];

  int attempts = 1;
  /* We found a possible matching key-value pair */
  while(item != NULL){
    if(item != &DELETED_ITEM)
    {
      if(strcmp(item->key, key) == 0){
        return item->value;
      }
    }

    /* If the keys are not equal, rehash the key and
     * check again */
    idx = get_hash(key, table->size, attempts);
    item = table->items[idx];
    attempts++;
  }

  /* No matching keys found at the hashed indices */
  return NULL; 
}

void entry_del(hash_table* table, const char* key){
  const int load = table->count / table->size;
  if(load < SIZE_DOWN_FACTOR){
    table_resize_down(table);
  }
  
  int idx = get_hash(key, table->size, 0);
  item_pair* item = table->items[idx];

  int attempts = 1;
  while(item != NULL){
    if(item != &DELETED_ITEM){
      if(strcmp(item->key, key) == 0){
        delete_item(item);
        /* Add a placeholder item */
        table->items[idx] = &DELETED_ITEM; 
        break; 
      }
    }

    idx = get_hash(key, table->size, attempts);
    item = table->items[idx];
    attempts++;
  }

  table->count--; 
}

static hash_table* resized_table(const int base_size){
  hash_table* table = (hash_table*) malloc(sizeof(hash_table) * 1);
 
  if(table == NULL){
    fprintf(stderr, "Error: unable to resize hash table!");
    exit(1);
  }
  table->base_size = base_size;
  table->size = next_prime(table->base_size);
  table->count = 0;
  table->items = (item_pair**) malloc(sizeof(item_pair*) * table->size);

  if(table->items == NULL){
    fprintf(stderr, "Error: uanble to allocate memory for hash array!");
    exit(1);
  }
  return table;
}

hash_table* new_table(){
  return resized_table(INITIAL_SIZE); 
}

static void resize(hash_table* table, const int base_size){
  if(base_size < INITIAL_SIZE){
    return;
  }

  hash_table* new_table = resized_table(base_size);
  for(size_t i = 0; i < table->size; i++){
    item_pair* item = table->items[i];
    if(item != NULL && item != &DELETED_ITEM){
      insert(new_table, item->key, item->value);
    }
  }

  table->base_size = new_table->base_size;
  table->count = new_table->count; 

  
  const int tmp_size = table->size;
  table->size = new_table->size;
  new_table->size = tmp_size; 

  item_pair** tmp_items = table->items;
  table->items = new_table->items; 
  new_table->items = tmp_items; 

  delete_table(new_table);
}

static void table_resize_up(hash_table* table){
  const int new_size = table->base_size * 2;
  resize(table, new_size);
}

static void table_resize_down(hash_table* table){
  const int new_size = table->base_size / 2;
  resize(table, new_size); 
}
