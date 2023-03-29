"""
方法二: 深度优先搜索(DFS) 之 "自顶向下" 的递归
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题模板：
1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
5. return the answer if needed                      // answer <-- left_ans, right_ans

适用场景：
当遇到树问题时，请先思考一下两个问题：
1. 如果你能确定一些参数，那么从该节点自身出发，你能计算出答案吗？
2. 你可以使用这些参数和节点自身的值来决定传递给它的左右子节点的参数吗？(depth + 1)

解题思路：
我们知道根节点的深度是 1。
对于每个节点，如果我们知道该节点的深度，那我们就可以知道它的左右子节点的深度。
因此，在调用递归函数的时候，将节点的深度传递为一个参数，那么所有的节点就都可以知道它们自身的深度。
而对于叶节点，我们可以通过更新深度从而获取最终的答案


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点在递归中只被遍历一次。
空间复杂度：O(h)，其中 h 是树的高度。空间复杂度主要取决于递归时栈空间的开销，最坏情况下，树呈现链状，空间复杂度为 O(n)。平均情况下树的高度与节点数的对数正相关，空间复杂度为 O(logn)。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0  # don't forget to initialize answer before call _dfs

        def _dfs(root: TreeNode, depth: int) -> None:
            if not root:
                return
            if not root.left and not root.right:  # leaf node
                nonlocal ans
                ans = max(ans, depth)  # update the answer if needed
            _dfs(root.left, depth + 1)
            _dfs(root.right, depth + 1)

        _dfs(root, 1)  # the depth of root node is 1
        return ans
