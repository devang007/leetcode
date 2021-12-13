# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order



def function(name):

    nums =[-5,-6,-4,-3,0,1,2,3,4]

    for i in range(len(nums)):
        nums[i] = nums[i]*nums[i]

    print(nums.sort())
    return nums.sort()
    # final=[]
    # left=0
    # right=len(nums)-1
    # final_pointer=len(nums)-1
    #
    # for i in range(len(nums)):
    #     final.append(0)
    #
    # while left <= right:
    #     print("l", left)
    #     print("r", right)
    #
    #     if abs(nums[left]) > abs(nums[right]):
    #         final[final_pointer]=nums[left]*nums[left]
    #         left=left+1
    #     else:
    #         final[final_pointer]=nums[right]*nums[right]
    #         right=right-1
    #     final_pointer =final_pointer-1
    #
    # return final

if __name__ == '__main__':
    print(function("func"))
