class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr.sort()
        ones = [0]*n
        for i in range(len(arr)):
            ones[i] = bin(arr[i]).count('1')
        for i in range(n-1):
            for j in range(n-1-i):
                if ones[j]>ones[j+1]:
                    ones[j],ones[j+1] = ones[j+1],ones[j]
                    arr[j],arr[j+1] = arr[j+1], arr[j]
        return arr
