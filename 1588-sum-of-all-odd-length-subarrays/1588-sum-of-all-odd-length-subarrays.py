class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        #holder = []
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n+1, 2):
                    #holder.append(arr[i:j])
                    ans += sum(arr[i:j])

        return ans