# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasGroupsSizeX(deck):  # 定义函数 hasGroupsSizeX（参数：deck）
    from collections import Counter  # from collections import Counter

    count = Counter(deck)  # 把 Counter(deck) 存入 计数
    result = list(set(count.values()))  # 把 列表(set(计数.values())) 存入 结果

    def gcd(a, b):  # 定义函数 gcd（参数：数组, b）
        while b:  # 循环，直到不满足「b」
            a, b = b, a % b  # 把 b, 数组 对…取模 b 写入 a, b
        return a  # 返回 数组

    while len(result) > 1:  # 循环，直到不满足「长度(结果) 超过 1」
        a = result.pop(0)  # 把 结果 弹出 0) 存入 数组
        b = result.pop(0)  # 把 结果 弹出 0) 存入 b
        result.insert(0, gcd(a, b))  # 结果 插入 0, gcd(数组, b))
    return result[0] > 1 if result else False  # 返回 结果[0] 超过 1 if 结果 else False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasGroupsSizeX(None))  # 打印输出
