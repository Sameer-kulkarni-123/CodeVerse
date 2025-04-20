class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        iflag = 0
        xflag = 0
        cflag = 0
        for c in s:
            if c == 'I':
                iflag = 1
                sum += 1
            elif c == 'V':
                if iflag:
                    sum += 3
                else:
                    sum += 5
            elif c == 'X':
                if iflag:
                    sum += 8
                else:
                    sum += 10
                    xflag = 1
            elif c == 'L':
                if xflag:
                    sum += 30
                else:
                    sum += 50
            elif c == 'C':
                if xflag:
                    sum += 80
                else:
                    sum += 100
                    cflag = 1

            elif c == 'D':
                if cflag:
                    sum += 300
                else:
                    sum += 500
            else:
                if cflag:
                    sum += 800
                else:
                    sum += 1000
        return sum

        