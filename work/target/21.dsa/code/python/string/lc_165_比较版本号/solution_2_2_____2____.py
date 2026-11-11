# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145246197
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def compareVersion(version1, version2):  # 定义函数 compareVersion（参数：version1, version2）
    v1 = version1.split(".")  # 把 version1.split('.') 存入 v1
    v2 = version2.split(".")  # 把 version2.split('.') 存入 v2
    len1, len2 = len(v1), len(v2)  # 把 长度(v1), 长度(v2) 写入 len1, len2
    max_len = max(len1, len2)  # 把 取较大值 len1, len2) 存入 max_len
    for i in range(max_len):  # 让 下标 i 从 max_len 遍历
        num1 = int(v1[i]) if i < len1 else 0  # 把 int(v1[下标 i]) if 下标 i 小于 len1 else 0 存入 num1
        num2 = int(v2[i]) if i < len2 else 0  # 把 int(v2[下标 i]) if 下标 i 小于 len2 else 0 存入 num2
        if num1 < num2:  # 若 num1 小于 num2
            return -1  # 返回 减 1
        elif num1 > num2:  # 否则，若 num1 超过 num2
            return 1  # 返回 1
    return 0  # 返回 0


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(compareVersion("1.01", "1.001"))  # 0
    print(compareVersion("1.0", "1.0.0"))  # 0
    print(compareVersion("0.1", "1.1"))  # -1
