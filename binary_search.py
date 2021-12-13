# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


def function(name):

    nums =[-1,0,3,5,9,12]
    target =-1
    l=0
    r=len(nums)-1
    while l <= r:
            middle=l + (r - l) // 2
            print("middle:",middle)

            print("middle check",nums[middle])
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target :
                r = middle - 1
    return -1








if __name__ == '__main__':
    function("func")
