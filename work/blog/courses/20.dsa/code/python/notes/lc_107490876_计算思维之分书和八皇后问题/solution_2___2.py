# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def allocate_books_func():  # 定义函数 allocate_books_func（参数：无）
    """分书问题（优化版 / 函数式状态传递）：不使用全局可变状态，
    每次递归用新的临时变量记录分配状态。"""
    like = [
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
    ]
    results = []  # 把 [] 存入 results

    def try_assign(reader, assigned):  # 定义函数 try_assign（参数：reader, assigned）
        if reader == 5:  # 若 reader 等于 5
            results.append(assigned)  # 把 assigned 追加到列表尾部
            return  # return
        for book in range(5):  # 让 book 从 5 遍历
            if (
                like[reader][book] == 1 and assigned[book] == -1
            ):  # 若 like[reader][book] 等于 1 and assigned[book] 等于 减 1
                nxt = assigned[:]  # 把 复制 assigned 存入 nxt
                nxt[book] = reader  # 把 reader 写入 nxt[book]
                try_assign(reader + 1, nxt)  # try_assign(reader 加 1, nxt)

    try_assign(0, [-1] * 5)  # try_assign(0, [ 减 1] 乘 5)
    return results  # 返回 results


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    res = allocate_books_func()  # 把 allocate_books_func() 存入 结果
    print("分书方案数:", len(res))  # 打印输出
    names = ["A", "B", "C", "D", "E"]  # 把 ['A', 'B', 'C', 'D', 'E'] 存入 names
    for scheme in res:  # 逐个取出 结果 的元素（scheme）
        print(" | ".join(f"书{i}->{names[scheme[i]]}" for i in range(5)))  # 打印输出
