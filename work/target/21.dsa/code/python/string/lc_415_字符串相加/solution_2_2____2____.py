# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381885
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def addStrings(num1, num2):  # 定义函数 addStrings（参数：num1, num2）
    i, j = len(num1) - 1, len(num2) - 1  # 把 长度(num1) 减 1, 长度(num2) 减 1 写入 i, j
    carry = 0  # 把 0 存入 carry
    result = []  # 把 [] 存入 结果
    while i >= 0 or j >= 0 or carry:  # 循环，直到不满足「下标 i 不低于 0 or 下标 j 不低于 0 or carry」
        total = carry  # 把 carry 存入 总和
        if i >= 0:  # 若 下标 i 不低于 0
            total += int(num1[i])  # 总和累加 int(num1[下标 i])
            i -= 1  # 下标 i累减 1
        if j >= 0:  # 若 下标 j 不低于 0
            total += int(num2[j])  # 总和累加 int(num2[下标 j])
            j -= 1  # 下标 j累减 1
        result.append(str(total % 10))  # 把 str(总和 对…取模 10 追加到列表尾部
        carry = total // 10  # 把 总和 除以 除以 10 存入 carry
    return "".join(reversed(result))  # 返回 ''.join(reversed(结果))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(addStrings("11", "123"))  # 打印输出
