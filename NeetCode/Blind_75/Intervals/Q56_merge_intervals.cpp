/* Question 56: Merge Intervals

Description: Given an array of intervals where intervals[i] = [starti, endi], 
             merge all overlapping intervals, and return an array of the 
             non-overlapping intervals that cover all the intervals in the 
             input.

Constraints:

                1 <= intervals.length <= 104
                0 <= starti <= endi   <= 104
                intervals[i].length == 2
*/
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <utility>

class Solution{
    public:
        std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals){
            if(intervals.size() == 1){
                return intervals;
            }

            // Sort the intervals 
            // std::sort(intervals.begin(), intervals.end());  -> shorter alternative method
            std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b){
                return a[0] < b[0]; // Sort in ascending order using first element 
            }); 

            std::vector<std::vector<int>> result {intervals[0]};
            for(const auto& range : intervals){
                int prev_l = result.back()[0]; 
                int prev_u = result.back()[1]; 

                if(range[0] <= prev_u){
                    result.back() = {prev_l, std::max(prev_u, range[1])};
                }
                else{
                    result.push_back(range);
                }
            }
            return result;
        }
};

/*##############################################################################
###############                  TEST CASES                     ###############
###############################################################################*/
void testMergeIntervals() {
    Solution solution;
    
    std::vector<std::pair<std::vector<std::vector<int>>, std::vector<std::vector<int>>>> testCases = {
        {{{1, 3}, {2, 6}, {8, 10}, {15, 18}}, {{1, 6}, {8, 10}, {15, 18}}},
        {{{1, 4}, {4, 5}}, {{1, 5}}},
        {{{1, 10}, {2, 3}, {4, 5}, {6, 7}, {8, 9}}, {{1, 10}}},
        {{{1, 3}}, {{1, 3}}},
        {{{1, 4}, {5, 6}}, {{1, 4}, {5, 6}}},
        {{{1, 4}, {0, 0}}, {{0, 0}, {1, 4}}}
    };

    for (auto& [intervals, expected] : testCases) {
        std::vector<std::vector<int>> result = solution.merge(intervals);
        assert(result == expected);
        std::cout << "Test case passed!" << std::endl;
    }

    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    testMergeIntervals();
    return 0;
}
