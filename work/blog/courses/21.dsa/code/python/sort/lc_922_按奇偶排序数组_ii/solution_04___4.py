# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortArrayByParityII(nums):  # 定义函数 sortArrayByParityII（参数：数组）
    evens = [x for x in nums if x % 2 == 0]  # 把 [x for x in 数组 if x 对…取模 2 等于 0] 存入 evens
    odds = [x for x in nums if x % 2 == 1]  # 把 [x for x in 数组 if x 对…取模 2 等于 1] 存入 odds
    res = []  # 把 [] 存入 结果
    for i in range(len(evens)):  # 让 下标 i 从 长度(evens 遍历
        res.append(evens[i])  # 把 evens[下标 i] 追加到列表尾部
        res.append(odds[i])  # 把 odds[下标 i] 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortArrayByParityII([4, 2, 5, 7]))  # 打印输出
    print(sortArrayByParityII([2, 3]))  # 打印输出
