# # Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]




def function(name):

    nums =[1,2,3,4,6,5,7]
    nums_copy=nums.copy()
    k=2
    subset=[]
    for i in range((len(nums))-k,len(nums)):
        print(i)
        subset.append(nums[i])
        nums_copy.remove(nums[i])
    subset.extend(nums_copy)
    return subset

if __name__ == '__main__':
    print(function("func"))
































