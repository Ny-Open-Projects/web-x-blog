# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347105
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve():  # 定义函数 solve（参数：无）
    """
    LeetCode 496. 下一个更大元素 I
    单调栈解法框架
    """

    pass  # pass


def nextGreaterElement(nums1, nums2):  # 定义函数 nextGreaterElement（参数：数组1, 数组2）
    """
    找到nums2中每个元素的下一个更大元素，返回在nums1中的对应结果
    """
    stack = []  # 把 [] 存入 栈
    greater_map = {}  # 把 {} 存入 greater_map

    # 单调栈找nums2中每个元素的下一个更大值
    for num in nums2:  # 逐个取出 数组2 的元素（num）
        while stack and stack[-1] < num:  # 循环，直到不满足「栈 and 栈[ 减 1] 小于 num」
            greater_map[stack.pop()] = num  # 弹出栈顶元素
        stack.append(num)  # 把 num 追加到列表尾部

    # 构建结果
    result = []  # 把 [] 存入 结果
    for num in nums1:  # 逐个取出 数组1 的元素（num）
        result.append(greater_map.get(num, -1))  # 把 greater_map 查找 num, 减 1 追加到列表尾部

    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    nums1 = [4, 1, 2]  # 把 [4, 1, 2] 存入 数组1
    nums2 = [1, 3, 4, 2]  # 把 [1, 3, 4, 2] 存入 数组2
    print(nextGreaterElement(nums1, nums2))  # 打印输出
