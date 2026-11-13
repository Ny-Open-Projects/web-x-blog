# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133279737
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def intersection(nums1, nums2):  # 定义函数 intersection（参数：数组1, 数组2）
    nums1.sort()  # 排序
    nums2.sort()  # 排序
    length1, length2 = len(nums1), len(nums2)  # 把 长度(数组1), 长度(数组2) 写入 length1, length2
    index1 = index2 = 0  # 把 index2 赋值为 0 存入 index1
    result = []  # 把 [] 存入 结果
    while (
        index1 < length1 and index2 < length2
    ):  # 循环，直到不满足「index1 小于 length1 and index2 小于 length2」
        num1, num2 = nums1[index1], nums2[index2]  # 把 数组1[index1], 数组2[index2] 写入 num1, num2
        if num1 == num2:  # 若 num1 等于 num2
            if not result or num1 != result[-1]:  # 若 not 结果 or num1 不等于 结果[ 减 1]
                result.append(num1)  # 把 num1 追加到列表尾部
            index1 += 1  # index1累加 1
            index2 += 1  # index2累加 1
        elif num1 < num2:  # 否则，若 num1 小于 num2
            index1 += 1  # index1累加 1
        else:  # 否则
            index2 += 1  # index2累加 1
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(intersection([1, 2, 2, 1], [2, 2]))  # 打印输出
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # 打印输出
