# 一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照如下规则记录彩灯装饰结果： 
# 
#  
#  第一层按照从左到右的顺序记录 
#  除第一层外每一层的记录顺序均与上一层相反。即第一层为从左到右，第二层为从右到左。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [8,17,21,18,null,null,6]
# 输出：[[8],[21,17],[18,6]]
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
#  Related Topics 树 广度优先搜索 二叉树 👍 314 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def decorateRecord(self,root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        stack = deque([root])
        mark = 1
        while stack:
            arr = []
            num = len(stack)

            for i in range(num):
                # 判断方向
                item = stack.popleft()
                arr.append(item.val)
                if item.left:
                    stack.append(item.left)
                if item.right:
                    stack.append(item.right)

            if mark % 2 == 0:  # 从右取
                arr.reverse()
            mark += 1
            result.append(arr)
        return result
# leetcode submit region end(Prohibit modification and deletion)
