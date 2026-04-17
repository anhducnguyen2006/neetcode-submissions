# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        qp = deque()
        qp.append(p)
        qq = deque()
        qq.append(q)
        while qp and qq:
            p1 = qp.popleft()
            p2 = qq.popleft()
            if p1 == None and p2 != None:
                return False
            if p1 != None and p2 == None:
                return False
            if p1 == None and p2 == None:
                continue
            if p1.val != p2.val:
                return False
            if p1:
                qp.append(p1.left)
                qp.append(p1.right)
            if p2:
                qq.append(p2.left)
                qq.append(p2.right)
        if qp or qq:
            return False
        return True