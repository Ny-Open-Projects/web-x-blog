# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def countBinarySubstrings(s):  # 定义函数 countBinarySubstrings（参数：字符串）
    groups = []  # 把 [] 存入 groups
    count = 1  # 把 1 存入 计数
    for i in range(1, len(s)):  # 让 下标 i 从 1 到 长度(字符串 遍历
        if s[i] == s[i - 1]:  # 若 字符串[下标 i] 等于 字符串[下标 i 减 1]
            count += 1  # 计数累加 1
        else:  # 否则
            groups.append(count)  # 把 计数 追加到列表尾部
            count = 1  # 把 1 存入 计数
    groups.append(count)  # 把 计数 追加到列表尾部
    return sum(min(groups[i], groups[i + 1]) for i in range(len(groups) - 1))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(countBinarySubstrings("abc"))  # 打印输出
