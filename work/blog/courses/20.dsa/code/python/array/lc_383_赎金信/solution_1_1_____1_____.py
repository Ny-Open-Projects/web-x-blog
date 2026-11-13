# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355797
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def canConstruct(ransomNote, magazine):  # 定义函数 canConstruct（参数：ransomNote, magazine）
    if len(ransomNote) > len(magazine):  # 若 长度(ransomNote) 超过 长度(magazine
        return False  # 返回 False
    cnt = [0] * 26  # 把 [0] 乘 26 存入 计数
    for c in magazine:  # 逐个取出 magazine 的元素（字符）
        cnt[ord(c) - ord("a")] += 1  # 把 1 写入 cnt[ord(c) - ord('a')] +
    for c in ransomNote:  # 逐个取出 ransomNote 的元素（字符）
        idx = ord(c) - ord("a")  # 把 ord(字符) 减 ord('数组') 存入 idx
        cnt[idx] -= 1  # cnt[idx]累减 1
        if cnt[idx] < 0:  # 若 计数[idx] 小于 0
            return False  # 返回 False
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(canConstruct("a", "b"))  # 打印输出
    print(canConstruct("aa", "ab"))  # 打印输出
    print(canConstruct("aa", "aab"))  # 打印输出
