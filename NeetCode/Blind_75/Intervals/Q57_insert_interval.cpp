/* Question 57: Insert Interval

Description: You are given an array of non-overlapping intervals intervals 
             where intervals[i] = [starti, endi] represent the start and the 
             end of the ith interval and intervals is sorted in ascending order 
             by starti. You are also given an interval newInterval = [start, end] 
             that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array 
and return it.

Constraints:

            0 <= intervals.length <= 104
            0 <= start            <= end  <= 105
            0 <= starti           <= endi <= 105

            intervals is sorted by starti in ascending order.
            intervals[i].length == 2
            newInterval.length == 2
*/
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

class Solution{
    public:
        std::vector<std::vector<int>> insert(std::vector<std::vector<int>>& intervals,
                                             std::vector<int>& newInterval){
            // Check empty intervals
            if(intervals.empty()){
                intervals.push_back(newInterval);
                return intervals; 
            }

            std::vector<std::vector<int>> result {}; 
            int elem_pos {}; 
            int length {static_cast<int>(intervals.size())};

            // Collect all the ranges before the new interval
            while(elem_pos < length && intervals[elem_pos][1] < newInterval[0]){
                result.push_back(intervals[elem_pos]);
                ++elem_pos; 
            }

            // Merge intervals that overlap with the new interval 
            while(elem_pos < length && intervals[elem_pos][0] <= newInterval[1]){
                newInterval[0] = std::min(newInterval[0], intervals[elem_pos][0]);
                newInterval[1] = std::max(newInterval[1], intervals[elem_pos][1]);
                ++elem_pos;
            }
            result.push_back(newInterval); // Essential operation, DO NOT forget! 

            // Collect all the ranges after the new interval 
            while(elem_pos < length){
                result.push_back(intervals[elem_pos]);
                ++elem_pos;
            }

            return result; 
        }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/

void printIntervals(const std::vector<std::vector<int>>& intervals) {
    std::cout << "[";
    for (size_t i = 0; i < intervals.size(); ++i) {
        std::cout << "[" << intervals[i][0] << "," << intervals[i][1] << "]";
        if (i != intervals.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]\n";
}

void testInsertInterval() {
    Solution solution;

    // Test case 1: New interval in the middle, overlapping
    std::vector<std::vector<int>> intervals1 = {{1, 3}, {6, 9}};
    std::vector<int> newInterval1 = {2, 5};
    std::vector<std::vector<int>> expected1 = {{1, 5}, {6, 9}};
    assert(solution.insert(intervals1, newInterval1) == expected1);

    // Test case 2: New interval before all others, no overlapping
    std::vector<std::vector<int>> intervals2 = {{3, 5}, {7, 9}};
    std::vector<int> newInterval2 = {1, 2};
    std::vector<std::vector<int>> expected2 = {{1, 2}, {3, 5}, {7, 9}};
    assert(solution.insert(intervals2, newInterval2) == expected2);

    // Test case 3: New interval after all others, no overlapping
    std::vector<std::vector<int>> intervals3 = {{1, 2}, {3, 5}};
    std::vector<int> newInterval3 = {6, 7};
    std::vector<std::vector<int>> expected3 = {{1, 2}, {3, 5}, {6, 7}};
    assert(solution.insert(intervals3, newInterval3) == expected3);

    // Test case 4: New interval overlapping all existing intervals
    std::vector<std::vector<int>> intervals4 = {{1, 2}, {3, 5}, {6, 7}};
    std::vector<int> newInterval4 = {0, 8};
    std::vector<std::vector<int>> expected4 = {{0, 8}};
    assert(solution.insert(intervals4, newInterval4) == expected4);

    // Test case 5: New interval merging multiple intervals in the middle
    std::vector<std::vector<int>> intervals5 = {{1, 2}, {3, 5}, {6, 9}};
    std::vector<int> newInterval5 = {4, 7};
    std::vector<std::vector<int>> expected5 = {{1, 2}, {3, 9}};
    assert(solution.insert(intervals5, newInterval5) == expected5);

    // Test case 6: No intervals initially
    std::vector<std::vector<int>> intervals6 = {};
    std::vector<int> newInterval6 = {5, 7};
    std::vector<std::vector<int>> expected6 = {{5, 7}};
    assert(solution.insert(intervals6, newInterval6) == expected6);

    // Test case 7: Single interval, no overlap
    std::vector<std::vector<int>> intervals7 = {{2, 3}};
    std::vector<int> newInterval7 = {4, 5};
    std::vector<std::vector<int>> expected7 = {{2, 3}, {4, 5}};
    assert(solution.insert(intervals7, newInterval7) == expected7);

    // Test case 8: Single interval, overlap and merge
    std::vector<std::vector<int>> intervals8 = {{2, 3}};
    std::vector<int> newInterval8 = {1, 4};
    std::vector<std::vector<int>> expected8 = {{1, 4}};
    assert(solution.insert(intervals8, newInterval8) == expected8);

    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    testInsertInterval();
    return 0;
}
