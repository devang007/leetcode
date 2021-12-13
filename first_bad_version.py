# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version.
# You should minimize the number of calls to the API.


def function(name):

    n=5
    l=1
    r=n
    bad=[]
    while l <= r:

            print("l:",l)
            print("r:", r)

            middle=l + (r - l) // 2
            copy_m=middle

            print("middle:",middle)
            if is_bad(middle):
                bad.append(copy_m)
                r = middle - 1
            else:
                l = middle + 1
    print(bad)
    return bad[-1]

def is_bad(version):
    if version==5:
        return True
    else:
        return False




if __name__ == '__main__':
    print(function("func"))