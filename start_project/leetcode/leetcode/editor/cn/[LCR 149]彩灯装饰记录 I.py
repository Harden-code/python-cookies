# 一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从 左 到 右 的顺序返回每一层彩灯编号。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [8,17,21,18,null,null,6]
# 输出：[8,17,21,18,6]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
# 
#  
# 
#  Related Topics 树 广度优先搜索 二叉树 👍 310 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def decorateRecord(self,root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        stack = deque([root])
        while stack:
            # 使用队列
            item = stack.popleft()
            result.append(item.val)
            if item.left:
                stack.append(item.left)
            if item.right:
                stack.append(item.right)
        return result

# leetcode submit region end(Prohibit modification and deletion)
