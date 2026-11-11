# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381943
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def multiply(num1, num2):  # 定义函数 multiply（参数：num1, num2）
    if num1 == "0" or num2 == "0":  # 若 num1 等于 「0」 or num2 等于 「0」
        return "0"  # 返回 「0」
    m, n = len(num1), len(num2)  # 把 长度(num1), 长度(num2) 写入 m, n
    result = [0] * (m + n)  # 把 [0] 乘 (映射表 加 元素个数) 存入 结果
    for i in range(m - 1, -1, -1):  # 让 下标 i 从 映射表 减 1 倒数回去（每步减 1）
        for j in range(n - 1, -1, -1):  # 让 下标 j 从 元素个数 减 1 倒数回去（每步减 1）
            mul = int(num1[i]) * int(num2[j])  # 把 int(num1[下标 i]) 乘 int(num2[下标 j]) 存入 mul
            p1, p2 = i + j, i + j + 1  # 把 下标 i 加 下标 j, 下标 i 加 下标 j 加 1 写入 p1, p2
            total = mul + result[p2]  # 把 mul 加 结果[p2] 存入 总和
            result[p2] = total % 10  # 把 总和 对…取模 10 写入 result[p2]
            result[p1] += total // 10  # result[p1]累加 总和 除以 除以 10
    return (
        "".join(str(d) for d in result).lstrip("0") or "0"
    )  # 返回 ''.join(str(d) for d in 结果).lstrip('0') or 「0」


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(multiply("2", "3"))  # 打印输出
    print(multiply("123", "456"))  # 打印输出
