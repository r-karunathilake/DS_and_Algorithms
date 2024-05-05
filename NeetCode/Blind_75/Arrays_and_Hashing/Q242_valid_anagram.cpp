/* Question 242: Valid Anagram 

Description: Given two strings s and t, return true if t is an anagram of s, 
             and false otherwise. An Anagram is a word or phrase formed by 
             rearranging the letters of a different word or phrase, typically 
             using all the original letters exactly once

Constraints:
        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.
*/

#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    bool isAnagram(const std::string& s, const std::string& t) {
        // Make sure the strings are the same length 
        if (s.size() != t.size())
            return false;
        
        // Count the frequency of characters in string 's'
        std::unordered_map<char, int> counter_s;
        for (const char c : s)
            counter_s[c]++;
        
        for (const char c : t) {
            if (counter_s.find(c) == counter_s.end() || counter_s[c] == 0)
                return false;
            
            // Decrement the character frequency 
            counter_s[c]--;
        }
        
        return true;
    }
};

int main() {
    Solution solution;
    std::string s = "anagram";
    std::string t = "nagaram";
    std::cout << std::boolalpha << solution.isAnagram(s, t) << std::endl; // Output: true
    return 0;
}
