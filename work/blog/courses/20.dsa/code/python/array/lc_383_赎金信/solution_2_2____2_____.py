# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355797
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def canConstruct(ransomNote, magazine):  # 定义函数 canConstruct（参数：ransomNote, magazine）
    arr = [0] * 26  # 把 [0] 乘 26 存入 数组
    base = ord("a")  # 把 ord('数组') 存入 base
    for m in magazine:  # 逐个取出 magazine 的元素（映射表）
        arr[ord(m) - base] += 1  # 把 1 写入 arr[ord(m) - base] +
    for r in ransomNote:  # 逐个取出 ransomNote 的元素（右指针）
        arr[ord(r) - base] -= 1  # 把 1 写入 arr[ord(r) - base] -
    return all(v >= 0 for v in arr)  # 返回 all(值 不低于 0 for 值 in 数组)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(canConstruct("a", "b"))  # 打印输出
    print(canConstruct("aa", "ab"))  # 打印输出
    print(canConstruct("aa", "aab"))  # 打印输出
