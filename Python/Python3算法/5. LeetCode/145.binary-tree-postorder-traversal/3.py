"""
方法三: 迭代
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/

解题思路：
使用「显示栈」来模拟递归中维护的「隐式系统栈」，由于栈是 "后进先出" 的顺序，所以入栈时先将根节点和它的所有子孙右节点入栈，这样得到的结果为「根、右、左」，再逆序输出就得到后序遍历的结果「左、右、根」。过程如下：
1. 初始化栈
2. cur 指向根节点，将它压栈(目的是后续将它出栈时能获取左子节点)
3. 如果 cur 有右子节点，将 cur 重新指向右子节点。重复步骤 2 (使用 while 循环)，直到 cur 为 None
4. 当 cur 为 None 时，弹出栈顶元素，此时才将它的值添加到结果中，并用 cur 重新指向它。获取它的左子节点，然后用 cur 重新指向左子节点。重复步骤 2 和 3 (使用另一个 while 循环)，直到栈为空


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被遍历一次。结果数组逆序操作也需要 O(n)
空间复杂度：取决于栈中存储的最大元素个数，其在最坏情况下会达到 O(n)。结果数组逆序操作只需要首尾两两原地交换即可
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = []  # 创建栈
        cur = root  # 开始时，cur 指向根节点
        while stack or cur:  # 需要加 or cur，因为一开始 stack 就是空的，但此时 cur 不为 None
            # 模拟递归遍历右子树(调用递归函数时需要将传入的参数压栈，这里使用显示栈来压入右节点)
            while cur:
                res.append(cur.val)  # 将 cur 的值添加到结果中
                stack.append(cur)  # 将 cur 压栈，目的是后续将它出栈时能获取左子节点
                cur = cur.right
            cur = stack.pop()  # 当 cur 为 None 时，弹出栈顶元素，并用 cur 重新指向它

            # 模拟递归遍历左子树(调用递归函数时需要将传入的参数压栈，这里使用显示栈来压入左节点)
            cur = cur.left  # 然后用 cur 重新指向它的左子节点

        # 逆序输出。或者使用另外一个栈，先进后出
        return res[::-1]
