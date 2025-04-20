
def longestConsecutive(nums):
    s = set()

    for n in nums:
        s.add(n)

    maxLen = 0
    count = 0

    for n in s:
        if n - 1 in s:
            continue
        else:
            temp = n
            while temp in s:
                count += 1
                temp += 1
            maxLen = max(count, maxLen)
            count = 0
    
    return maxLen
