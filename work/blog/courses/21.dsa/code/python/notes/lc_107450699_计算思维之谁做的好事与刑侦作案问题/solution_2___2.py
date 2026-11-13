# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def who_did_good():  # 定义函数 who_did_good（参数：无）
    # 思路二：通过数字表示人 (0=A,1=B,2=C,3=D)
    # A说:不是我  -> k != 0
    # B说:是C     -> k == 2
    # C说:是D     -> k == 3
    # D说:他胡说  -> k != 3
    for k in range(4):  # 让 下标 k 从 4 遍历
        s = (k != 0) + (k == 2) + (k == 3) + (k != 3)
        if s == 3:  # 若 字符串 等于 3
            print("做好事者为", chr(ord("A") + k))  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    who_did_good()  # 输出: 做好事者为 C
