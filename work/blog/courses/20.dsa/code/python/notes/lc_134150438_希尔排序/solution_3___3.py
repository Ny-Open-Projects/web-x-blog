# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def shell_sort(lst):  # 定义函数 shell_sort（参数：lst）
    length = len(lst)  # 把 长度(lst) 存入 长度
    gap = length // 2  # 把 长度 除以 除以 2 存入 gap
    while gap > 0:  # 循环，直到不满足「gap 超过 0」
        for i in range(gap, length):  # 让 下标 i 从 gap 到 长度 遍历
            temp = lst[i]  # 把 lst[下标 i] 存入 临时变量
            p = i  # 把 下标 i 存入 节点
            while (
                p >= gap and lst[p - gap] > temp
            ):  # 循环，直到不满足「节点 不低于 gap and lst[节点 减 gap] 超过 临时变量」
                lst[p] = lst[p - gap]  # 把 lst[节点 减 gap] 写入 lst[p]
                p -= gap  # 节点累减 gap
            lst[p] = temp  # 把 临时变量 写入 lst[p]
        gap //= 2  # 把 2 写入 gap //
    return lst  # 返回 lst


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    list_ = [9, 12, 1, 3, -1, 22, 22, 31, 1, 0]  # 把 [9, 12, 1, 3, 减 1, 22, 22, 31, 1, 0] 存入 list_
    shell_sort(list_)  # shell_sort(list_)
    print("list: ", list_)  # 打印输出
