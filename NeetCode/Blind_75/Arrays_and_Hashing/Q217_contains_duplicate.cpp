#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

#include <catch2/catch_test_macros.hpp>

/* Question 217: Contains Duplicate 

Description: Given an integer array nums, return true if any value appears at 
             least twice in the array, and return false if every element is 
             distinct.

Constraints:
               1 <= nums.length <= 10^5
           -10^9 <= nums[i]     <= 10^9
*/

/* Solution #1: 
        Time Complexity: O(N * logN)
        Space Complexity: O(1) 
*/
bool containsDuplicateOne(std::vector<int>&& nums){
    std::sort(nums.begin(), nums.end()); 
    return std::adjacent_find(nums.begin(), nums.end()) != nums.end(); 
}

/* Solution #2:
        Time Complexity: O(N)
        Space Complexity: O(N)
*/

bool containsDuplicateTwo(const std::vector<int>& nums){
    std::unordered_map<int, int> counter {}; 
    for(const auto num : nums){
        ++counter[num];
    }
    for(const auto item : counter){
        if(item.second >= 2){
            return true;
        }
    }
    // No duplicates found! 
    return false;
}

/*
###############################################################################
###############                  TEST CASES                     ###############
###############################################################################
*/
TEST_CASE("Test the first solution"){
    REQUIRE( containsDuplicateOne(std::vector<int> {1, 2, 3}) == false );
    REQUIRE( containsDuplicateOne(std::vector<int> {1, 2, 3, 1}) == true );
}

TEST_CASE("Test the second solution"){
    REQUIRE( containsDuplicateTwo(std::vector<int> {1, 2, 3}) == false );
    REQUIRE( containsDuplicateTwo(std::vector<int> {1, 2, 3, 1}) == true );
}

