# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def asymptotic_example():  # 定义函数 asymptotic_example（参数：无）
    """例：T(n) = 5n·[3n·(n+2)+4] + 6 = 35n^3 + 30n^2 + 20n + 6  => O(n^3)。"""
    print("T(n) = 5n·[3n·(n+2)+4] + 6 的增长：")  # 打印输出
    for n in [1, 10, 100, 1000]:  # for 元素个数 in [1, 10, 100, 1000]:
        t = (
            5 * n * (3 * n * (n + 2) + 4) + 6
        )  # 把 5 乘 元素个数 乘 (3 乘 元素个数 乘 (元素个数 加 2) 加 4) 加 6 存入 另一字符串
        print(f"  n={n:5d}  T(n)={t}")  # 打印输出
    print("  => 主导项为 n^3，故 T(n) = O(n^3)")


def compare_constants_and_low_order():  # 定义函数 compare_constants_and_low_order（参数：无）
    """Big-O 忽略常数因子与低次项：n^2 与 2n^2+1000n 同阶 O(n^2)。"""
    print("\n忽略常数与低次项：")  # 打印输出
    for n in [10, 100, 1000]:  # for 元素个数 in [10, 100, 1000]:
        a = n * n  # 把 元素个数 乘 元素个数 存入 数组
        b = 2 * n * n + 1000 * n  # 把 2 乘 元素个数 乘 元素个数 加 1000 乘 元素个数 存入 b
        print(f"  n={n:5d}  n^2={a:8d}  2n^2+1000n={b:8d}  (同阶 O(n^2))")  # 打印输出


def classify(coeffs):  # 定义函数 classify（参数：coeffs）
    """给定各次项系数（索引为次数），返回最高次非零项对应的 Big-O 记号。"""
    for deg in range(len(coeffs) - 1, -1, -1):  # 让 deg 从 长度(coeffs) 减 1 倒数回去（每步减 1）
        if coeffs[deg] != 0:  # 若 coeffs[deg] 不等于 0
            return f"O(n^{deg})" if deg > 1 else ("O(n)" if deg == 1 else "O(1)")
    return "O(1)"  # 返回 「O(1)」


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    asymptotic_example()  # asymptotic_example()
    compare_constants_and_low_order()  # compare_constants_and_low_order()
    print("\nclassify([6, 20, 30, 35]) =", classify([6, 20, 30, 35]), "(对应 35n^3+30n^2+20n+6)")  # 打印输出
