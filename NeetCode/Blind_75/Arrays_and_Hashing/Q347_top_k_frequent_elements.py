""" Question 347: Top K Frequent Elements

Description: Given an integer array nums and an integer k, return the k most 
             frequent elements. You may return the answer in any order

Constraints:
               1 <= nums.length <= 10^5
           -10^4 <= nums[i]     <= 10^4
           
Note: k is in the range [1, the number of unique elements in the array].It is 
      guaranteed that the answer is unique. 

Note: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
"""


""" Solution #1: 

   Time complexity: O(N * logN) 
   Space complexity: O(N)
"""
from collections import Counter
def topKFrequent(nums: list[int], k: int) -> list[int]:
    counter = Counter(nums)

    top_k = sorted(counter.keys(), key=lambda num: counter[num], reverse=True)[:k]
    
    return top_k 


""" Solution #2: 

   Time complexity: O(N) 
   Space complexity: O(N)
"""
def topKFrequent(nums: list[int], k: int) -> list[int]:
    counter = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in counter.items():
        buckets[freq].append(num)

    results = [] 
    for idx in range(len(buckets) - 1, 0, -1):
        results.extend(buckets[idx])

        # Because of the extend() call, results may be longer than k if
        # multiple numbers have the same frequency. See test case #3 below. 
        if len(results) >= k:
            break

    return results[:k]

###############################################################################
###############                  TEST CASES                     ###############
###############################################################################

import unittest 

class TestGroupAnagrams(unittest.TestCase):
    def test_single_item_list(self):
        nums = [1]
        self.assertEqual(topKFrequent(nums, 1), [1])

    def test_two(self):
        nums = [1, 2, 3, 3, 3, 5, 7, 5]
        self.assertEqual(topKFrequent(nums, 2), [3, 5])


    def test_three(self):
        nums = [1, 2, 4, 4, 5, 7, 5, 3]
        # Note: there are multiple answers for this case 
        self.assertEqual(topKFrequent(nums, 3), [4, 5, 1])

if __name__ == "__main__":
    unittest.main() 
