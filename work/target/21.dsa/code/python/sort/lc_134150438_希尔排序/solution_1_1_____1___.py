# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
def shell_sort(lst: list) -> None:  # 定义函数 shell_sort（参数：lst: 列表）
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


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    arr = [12, 34, 54, 2, 3]  # 把 [12, 34, 54, 2, 3] 存入 数组
    shell_sort(arr)  # shell_sort(数组)
    print(arr)  # 打印输出
