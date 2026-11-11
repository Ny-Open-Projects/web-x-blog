# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def countBinarySubstrings(s):  # 定义函数 countBinarySubstrings（参数：字符串）
    groups = []  # 把 [] 存入 groups
    i = 0  # 把 0 存入 下标 i
    n = len(s)  # 把 长度(字符串) 存入 元素个数
    while i < n:  # 循环，直到不满足「下标 i 小于 元素个数」
        ch = s[i]  # 把 字符串[下标 i] 存入 字符
        cnt = 0  # 把 0 存入 计数
        while i < n and s[i] == ch:  # 循环，直到不满足「下标 i 小于 元素个数 and 字符串[下标 i] 等于 字符」
            cnt += 1  # 计数累加 1
            i += 1  # 下标 i累加 1
        groups.append(cnt)  # 把 计数 追加到列表尾部
    ans = 0  # 把 0 存入 答案
    for j in range(1, len(groups)):  # 让 下标 j 从 1 到 长度(groups 遍历
        ans += min(groups[j - 1], groups[j])  # 答案累加 取较小值 groups[下标 j 减 1], groups[下标 j])
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(countBinarySubstrings("00110011"))  # 打印输出
    print(countBinarySubstrings("10101"))  # 打印输出
