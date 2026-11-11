# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370292
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def checkInclusion(s1, s2):  # 定义函数 checkInclusion（参数：s1, s2）
    if len(s1) > len(s2):  # 若 长度(s1) 超过 长度(s2
        return False  # 返回 False
    s1_count = [0] * 26  # 把 [0] 乘 26 存入 s1_count
    s2_count = [0] * 26  # 把 [0] 乘 26 存入 s2_count
    for i in range(len(s1)):  # 让 下标 i 从 长度(s1 遍历
        s1_count[ord(s1[i]) - ord("a")] += 1  # 把 1 写入 s1_count[ord(s1[i]) - ord('a')] +
        s2_count[ord(s2[i]) - ord("a")] += 1  # 把 1 写入 s2_count[ord(s2[i]) - ord('a')] +
    if s1_count == s2_count:  # 若 s1_count 等于 s2_count
        return True  # 返回 True
    for i in range(len(s1), len(s2)):  # 让 下标 i 从 长度(s1 遍历
        s2_count[ord(s2[i]) - ord("a")] += 1  # 把 1 写入 s2_count[ord(s2[i]) - ord('a')] +
        s2_count[
            ord(s2[i - len(s1)]) - ord("a")
        ] -= 1  # 把 1 写入 s2_count[ord(s2[i - len(s1)]) - ord('a')] -
        if s1_count == s2_count:  # 若 s1_count 等于 s2_count
            return True  # 返回 True
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(checkInclusion("ab", "eidbaooo"))  # 打印输出
