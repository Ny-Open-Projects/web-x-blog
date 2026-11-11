# 来源（blog）：二进制求和 — bin(int(a,2) + int(b,2)) 直接按二进制相加
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def add_binary(a, b):  # 定义函数 add_binary（参数：数组, b）
    return bin(int(a, 2) + int(b, 2))[2:]  # 返回 bin(int(数组, 2) 加 int(b, 2))[2:]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
    ]
    for a, b, want in cases:  # for 数组, b, want in cases:
        got = add_binary(a, b)  # 把 add_binary(数组, b) 存入 got
        assert got == want, f"addBinary({a},{b})={got} want {want}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
