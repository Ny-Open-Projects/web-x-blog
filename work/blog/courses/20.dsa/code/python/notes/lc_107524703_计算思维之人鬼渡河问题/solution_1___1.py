# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def is_safe(r, g):  # 定义函数 is_safe（参数：右指针, g）
    """人鬼渡河安全性判定（东岸人数 r、鬼数 g）：
    人数等于 3、等于 0，或与鬼数相等时安全。"""
    return 0 <= r <= 3 and 0 <= g <= 3 and (r == 0 or r == 3 or r == g)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    for state in [
        (3, 3),
        (3, 1),
        (2, 2),
        (1, 3),
        (0, 0),
    ]:  # for state in [(3, 3), (3, 1), (2, 2), (1, 3), (0, 0)]:
        print(state, "->", "安全" if is_safe(*state) else "不安全")  # 打印输出
