def twoSum(nums, target):
    visited = {}
    for i in range(len(nums)):
        if target - nums[i] in visited.keys():
            return [visited[target-nums[i]], i]
        else:
            visited[nums[i]] = i  