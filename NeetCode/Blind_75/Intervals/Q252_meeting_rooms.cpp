/* Question 252: Meeting Rooms

Description: Given an array of meeting time interval objects consisting of start 
             and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
             determine if a person could add all meetings to their schedule 
             without any conflicts.

             Note: (0,8),(8,10) is not considered a conflict at 8

Constraints:

              0 <= intervals.length   <= 100
              0 <= intervals[i].start < intervals[i].end <= 1000
*/

class Interval{
    public:
        int start, end {};
        Interval(int start, int end) : start(start), end(end) {}
};

#include <algorithm>
#include <vector>
#include <cassert>
#include <iostream>

class Solution{
    public:
        bool canAttendMeetings(std::vector<Interval>& intervals){
            // Sort all the intervals based on the start time 
            std::sort(intervals.begin(), intervals.end(), [](const Interval &a, const Interval &b){
                return a.start < b.start;
            });

            int end   {};
            for(const auto& interval : intervals){
                if(interval.start < end){
                    return false; 
                }
                end = interval.end ;
            }
            return true; 
        }
};

void runTestCases() {
    Solution solution;

    // Test Case 1: No overlap
    std::vector<Interval> intervals1 = {Interval(0, 30), Interval(35, 40), Interval(45, 50)};
    assert(solution.canAttendMeetings(intervals1) == true);
    std::cout << "Test Case 1 Passed" << std::endl;

    // Test Case 2: Overlap exists
    std::vector<Interval> intervals2 = {Interval(0, 30), Interval(25, 35), Interval(40, 50)};
    assert(solution.canAttendMeetings(intervals2) == false);
    std::cout << "Test Case 2 Passed" << std::endl;

    // Test Case 3: Single meeting
    std::vector<Interval> intervals3 = {Interval(0, 30)};
    assert(solution.canAttendMeetings(intervals3) == true);
    std::cout << "Test Case 3 Passed" << std::endl;

    // Test Case 4: Empty intervals
    std::vector<Interval> intervals4 = {};
    assert(solution.canAttendMeetings(intervals4) == true);
    std::cout << "Test Case 4 Passed" << std::endl;

    // Test Case 5: Adjacent meetings
    std::vector<Interval> intervals5 = {Interval(0, 10), Interval(10, 20), Interval(20, 30)};
    assert(solution.canAttendMeetings(intervals5) == true);
    std::cout << "Test Case 5 Passed" << std::endl;
}

int main() {
    runTestCases();
    std::cout << "All test cases passed!" << std::endl;
    return 0;
}
