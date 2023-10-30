class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def help(num):
            bit = bin(num).count('1')
            return (bit, num)
        arr.sort(key = help)
        return arr
