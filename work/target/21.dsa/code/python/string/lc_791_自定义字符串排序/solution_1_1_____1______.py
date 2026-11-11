# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370193
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def customSortString(order, s):  # 定义函数 customSortString（参数：order, 字符串）
    count = {}  # 把 {} 存入 计数
    for c in s:  # 逐个取出 字符串 的元素（字符）
        count[c] = count.get(c, 0) + 1  # 把 计数 查找 字符, 0) 加 1 写入 count[c]
    result = []  # 把 [] 存入 结果
    for c in order:  # 逐个取出 order 的元素（字符）
        if c in count:  # 若 字符 in 计数
            result.append(c * count[c])  # 把 字符 乘 计数[字符] 追加到列表尾部
            del count[c]  # del 计数[字符]
    for c in count:  # 逐个取出 计数 的元素（字符）
        result.append(c * count[c])  # 把 字符 乘 计数[字符] 追加到列表尾部
    return "".join(result)  # 返回 ''.join(结果)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(customSortString("cba", "abcd"))  # 打印输出
    print(customSortString("cbafg", "abcd"))  # 打印输出
