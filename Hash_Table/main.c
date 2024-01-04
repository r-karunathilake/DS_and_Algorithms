#include "hash_table.h"

int main(int argc, char* argv[]){
  hash_table* table = init_hash_table(); 
  delete_table(table);

  return 0;
}
