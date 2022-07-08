# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum_ = 0
        
        def traverse(r):
            if r: 
                if r.val >= low:
                    traverse(r.left)
                if low<= r.val <=high:
                    self.sum_ += r.val
                if r.val < high:
                    traverse(r.right)
            return self.sum_
        
        return traverse(root)
            
            
        """        
            if r.left:
                if r.val <= low: 
                    sum+=r.val
                    print(r.val)

                    
                sum += traverse(r.left)
                    
                    
            if low >= r.val <= high:
                sum += r.val
                
            if r.right:
                if low <= r.val <= high: 
                    sum += traverse(r.right)
                
            return sum
        return traverse(root)
   


  while node.left:
            if node.left.val >= low:
                sum += self.node.val
            self.node.next()
        
        while self.right:
            if self.right.val <= high: 
                sum += self.right.val
            self.right.next()
            
        """