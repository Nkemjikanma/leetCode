class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        holder = []
        for i in range(n):
            holder.append(nums[i])
            holder.append(nums[i + n])
        return holder
            
            