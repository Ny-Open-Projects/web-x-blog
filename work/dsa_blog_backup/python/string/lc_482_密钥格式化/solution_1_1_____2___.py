# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374443
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def licenseKeyFormatting(s, k):  # 定义函数 licenseKeyFormatting（参数：字符串, 下标 k）
    s = s.replace("-", "").upper()  # 把 字符串.replace(' 减 ', '').upper() 存入 字符串
    result = []  # 把 [] 存入 结果
    for i in range(len(s) - 1, -1, -1):  # 让 下标 i 从 长度(字符串) 减 1 倒数回去（每步减 1）
        result.append(s[i])  # 把 字符串[下标 i] 追加到列表尾部
        if (
            len(result) - 1
        ) % k == k - 1 and i > 0:  # 若 长度(结果) 减 1) 对…取模 下标 k 等于 下标 k 减 1 and 下标 i 超过 0
            result.append("-")  # 把 ' 减 ' 追加到列表尾部
    return "".join(reversed(result))  # 返回 ''.join(reversed(结果))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(licenseKeyFormatting("abc", 1))  # 打印输出
