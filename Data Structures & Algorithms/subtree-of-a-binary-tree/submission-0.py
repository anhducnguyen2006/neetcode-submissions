# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from collections import deque
        q = deque([root])
        while q:
            curr = q.popleft()
            if not curr: 
                continue
            if curr.val == subRoot.val:
                t = deque([(curr, subRoot)])
                ok = True
                while t:
                    c1, c2 = t.popleft()
                    if not c1 and not c2:
                        continue
                    if not c1 or not c2 or c1.val != c2.val:
                        ok = False
                        break
                    t.append((c1.left, c2.left))
                    t.append((c1.right, c2.right))
                if not t and ok:
                    return True
            q.append(curr.left)
            q.append(curr.right)
        return False
            