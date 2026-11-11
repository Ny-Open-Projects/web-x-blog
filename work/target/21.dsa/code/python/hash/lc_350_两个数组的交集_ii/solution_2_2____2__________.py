# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def intersect(nums1, nums2):  # 定义函数 intersect（参数：数组1, 数组2）
    nums1.sort()  # 排序
    nums2.sort()  # 排序
    res = []  # 把 [] 存入 结果
    i = j = 0  # 把 下标 j 赋值为 0 存入 下标 i
    while i < len(nums1) and j < len(
        nums2
    ):  # 循环，直到不满足「下标 i 小于 长度(数组1) and 下标 j 小于 长度(数组2」
        if nums1[i] < nums2[j]:  # 若 数组1[下标 i] 小于 数组2[下标 j]
            i += 1  # 下标 i累加 1
        elif nums1[i] > nums2[j]:  # 否则，若 数组1[下标 i] 超过 数组2[下标 j]
            j += 1  # 下标 j累加 1
        else:  # 否则
            res.append(nums1[i])  # 把 数组1[下标 i] 追加到列表尾部
            i += 1  # 下标 i累加 1
            j += 1  # 下标 j累加 1
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(intersect([1, 2, 2, 1], [2, 2]))  # 打印输出
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # 打印输出
