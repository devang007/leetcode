# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


def function(name):

    nums =[-1,0,3,5,9,12]
    target =11
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
    return l


if __name__ == '__main__':
    print(function("func"))
