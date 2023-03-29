"""
方法二：堆

解题思路：
我们用一个大顶堆实时维护数组的前 k 小值。
1. 首先将前 k 个数插入大顶堆中
2. 随后从第 k+1 个数开始遍历：
    如果当前遍历到的数比大顶堆的堆顶的数要大，则跳过它继续遍历(肯定不是前 k 小值，因为它比大顶堆最大的值还大)
    如果当前遍历到的数比大顶堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。
3. 最后将大顶堆里的数存入数组返回即可。

注意：Python 语言中的 heapq 模块创建的是小顶堆，因此我们要对数组中所有的数取负数，使用小顶堆找到前 k 大值，再将小顶堆里的数全部取反即可。
1. 首先将前 k 个数取反，再插入小顶堆中
2. 随后从第 k+1 个数开始遍历：
    如果当前遍历到的数取反后，比小顶堆的堆顶的数要小，则跳过它继续遍历(肯定不是前 k 大值，因为它比小顶堆最小的值还小)
    如果当前遍历到的数取反后，比小顶堆的堆顶的数要大，就把堆顶的数弹出，再插入当前遍历到的数的负数。
3. 最后将小顶堆里的数全部取反，再存入数组返回即可。

复杂度分析：
时间复杂度：O(nlogk)，其中 n 是数组 arr 的长度。由于小顶堆实时维护前 k 大值，所以插入删除都是 O(logk) 的时间复杂度，最坏情况下数组里 n 个数都会被依次插入，所以一共需要 O(nlogk) 的时间复杂度。
空间复杂度：O(k)，因为小顶堆里最多 k 个数。
"""
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        # 将前 k 个数取反，构建小顶堆
        h = [-x for x in arr[:k]]
        heapq.heapify(h)

        for i in range(k, len(arr)):
            if -arr[i] > h[0]:  # 如果当前遍历到的数取反后，比小顶堆的堆顶的数要大
                # heapq.heappop(h)  # 把堆顶的数弹出
                # heapq.heappush(h, -arr[i])  # 再插入当前遍历到的数的负数
                heapq.heapreplace(h, -arr[i])  # 等同于上面两行代码，但是只会重新进行一次堆化操作，效率更高！

        # 将小顶堆里的数全部取反，再存入数组返回
        ans = [-x for x in h]
        return ans
