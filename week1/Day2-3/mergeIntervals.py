class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort(key=lambda intervals: intervals[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastRes = res[-1]

            if not start > lastRes[1]:
                lastRes[1] = max(lastRes[1], end)
            else:
                res.append([start, end])

        return res
        

