# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def who_did_good():  # 定义函数 who_did_good（参数：无）
    # 思路一：通过字符表示人 (A/B/C/D)
    # A说:不是我  -> thisman != 'A'
    # B说:是C     -> thisman == 'C'
    # C说:是D     -> thisman == 'D'
    # D说:他胡说  -> thisman != 'D'
    # 已知三人说真话一人说假话：sum == 3
    found = False  # 把 False 存入 found
    for k in range(4):  # 让 下标 k 从 4 遍历
        thisman = chr(ord("A") + k)  # 把 chr(ord('A') 加 下标 k) 存入 thisman
        s = (thisman != "A") + (thisman == "C") + (thisman == "D") + (thisman != "D")
        if s == 3:  # 若 字符串 等于 3
            print("做好事者为", thisman)  # 打印输出
            found = True  # 把 True 存入 found
    if not found:  # 若 not found
        print("找不出做好事者")  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    who_did_good()  # 输出: 做好事者为 C
