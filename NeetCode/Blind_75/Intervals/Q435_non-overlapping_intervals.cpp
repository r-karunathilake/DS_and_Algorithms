/* Question 435: Non-overlapping intervals 

Description: Given an array of intervals where intervals[i] = [starti, endi], 
             return the minimum number of intervals you need to remove to make 
             the rest of the intervals non-overlapping.

Constraints:

           intervals[i].length == 2
           1 <= intervals.length <= 105
    -5 * 104 <= starti < endi    <= 5 * 104
*/
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

class Solution{
    public:
        int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals){
            // If there are no intervals, no need to remove anything
            if (intervals.empty()) return 0;

            // Sort the ranges 
            std::sort(intervals.begin(), intervals.end());

            int count {};
            int u_bound {intervals[0][1]};

            for(size_t i {1}; i < intervals.size(); ++i){
                std::vector<int> current_range = intervals[i];
                if(current_range[0] >= u_bound){
                    u_bound = current_range[1]; // Update upper bound 
                }
                else{ // We found an overlapping interval
                    ++count;
                    /* Minimum values is chosen for the 'end' b/c we need
                    to minimize the number of intervals we need to remove.
                    
                    e.g.

                    we keep track of e3 = min(e3, e1) b/c we should remove 
                    interval [s1, e1] to minimize the number of intervals we need
                    to remove. 
                                      |
                                      v          
                                    s2---e3  
                                s1----------e1 s3------e3 
                    */
                    u_bound = std::min(current_range[1], u_bound); // Essential update 
                }
            }
            return count; 
        }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/

void testEraseOverlapIntervals() {
    Solution sol;

    // Test case 1: No intervals
    std::vector<std::vector<int>> intervals1 = {};
    assert(sol.eraseOverlapIntervals(intervals1) == 0);

    // Test case 2: No overlapping intervals
    std::vector<std::vector<int>> intervals2 = {{1, 2}, {3, 4}, {5, 6}};
    assert(sol.eraseOverlapIntervals(intervals2) == 0);

    // Test case 3: All intervals overlap with each other
    std::vector<std::vector<int>> intervals3 = {{1, 3}, {2, 4}, {3, 5}};
    assert(sol.eraseOverlapIntervals(intervals3) == 1);

    // Test case 4: Some intervals overlap
    std::vector<std::vector<int>> intervals4 = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
    assert(sol.eraseOverlapIntervals(intervals4) == 1);

    // Test case 5: Intervals with same start and end times
    std::vector<std::vector<int>> intervals5 = {{1, 2}, {1, 2}, {1, 2}};
    assert(sol.eraseOverlapIntervals(intervals5) == 2);

    // Test case 6: Intervals with overlapping at edges
    std::vector<std::vector<int>> intervals6 = {{1, 2}, {2, 3}, {2, 4}};
    assert(sol.eraseOverlapIntervals(intervals6) == 1);

    // Test case 7: Large non-overlapping intervals
    std::vector<std::vector<int>> intervals7 = {{1, 100}, {101, 200}, {201, 300}};
    assert(sol.eraseOverlapIntervals(intervals7) == 0);

    // Test case 8: Overlapping intervals of varying lengths
    std::vector<std::vector<int>> intervals8 = {{1, 10}, {2, 3}, {4, 5}, {6, 7}, {8, 9}};
    assert(sol.eraseOverlapIntervals(intervals8) == 1);

    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    testEraseOverlapIntervals();
    return 0;
}
