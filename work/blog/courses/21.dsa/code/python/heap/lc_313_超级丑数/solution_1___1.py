# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def nthSuperUglyNumber(n, primes):  # 定义函数 nthSuperUglyNumber（参数：元素个数, primes）
    res = [1]  # 把 [1] 存入 结果
    i = 2  # 把 2 存入 下标 i
    while len(res) < n:  # 循环，直到不满足「长度(结果) 小于 元素个数」
        l = 0  # 把 0 存入 左指针
        for j in range(i):  # 让 下标 j 从 下标 i 遍历
            if i % j == 0 and j not in primes:  # 若 下标 i 对…取模 下标 j 等于 0 and 下标 j not in primes
                break  # 跳出循环
            l += 1  # 左指针累加 1
        if l == 0:  # 若 左指针 等于 0
            if any(item == i for item in primes):  # 若 any(item 等于 下标 i for item in primes
                res.append(i)  # 把 下标 i 追加到列表尾部
        else:  # 否则
            res.append(i)  # 把 下标 i 追加到列表尾部
        i += 1  # 下标 i累加 1
    return res[n - 1]  # 返回 结果[元素个数 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(nthSuperUglyNumber(1, None))  # 打印输出
