# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr:
                q.append(curr.left)
                q.append(curr.right)
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
        return root