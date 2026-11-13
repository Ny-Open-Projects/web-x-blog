# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def allocate_books():  # 定义函数 allocate_books（参数：无）
    """分书问题（基础回溯）：把 5 本书分给 A~E 五人，每人都分到自己感兴趣的书。
    like[reader][book] == 1 表示 reader 喜欢 book。返回所有分配方案（assigned[book]=reader）。"""
    like = [
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
    ]
    assigned = [-1] * 5  # 把 [ 减 1] 乘 5 存入 assigned
    results = []  # 把 [] 存入 results

    def try_assign(reader):  # 定义函数 try_assign（参数：reader）
        if reader == 5:  # 若 reader 等于 5
            results.append(assigned[:])  # 把 复制 assigned 追加到列表尾部
            return  # return
        for book in range(5):  # 让 book 从 5 遍历
            if (
                like[reader][book] == 1 and assigned[book] == -1
            ):  # 若 like[reader][book] 等于 1 and assigned[book] 等于 减 1
                assigned[book] = reader  # 把 reader 写入 assigned[book]
                try_assign(reader + 1)  # try_assign(reader 加 1)
                assigned[book] = -1  # 回溯

    try_assign(0)  # try_assign(0)
    return results  # 返回 results


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    res = allocate_books()  # 把 allocate_books() 存入 结果
    print("分书方案数:", len(res))  # 打印输出
    names = ["A", "B", "C", "D", "E"]  # 把 ['A', 'B', 'C', 'D', 'E'] 存入 names
    for scheme in res:  # 逐个取出 结果 的元素（scheme）
        print(" | ".join(f"书{i}->{names[scheme[i]]}" for i in range(5)))  # 打印输出
