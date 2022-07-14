# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = {}
        
        if head is None: 
            return False
        while head:
            head = head.next
            if head in count: 
                count[head] += 1
            else: 
                count.setdefault(head, 1)
            
            if count[head] > 1:
                return True
            
        return False
            
        
        