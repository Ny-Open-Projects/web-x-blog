# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374488
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def areNumbersAscending(s):  # 定义函数 areNumbersAscending（参数：字符串）
    words = s.split()  # 把 字符串.split() 存入 单词列表
    prev = 0  # 把 0 存入 前一个
    for word in words:  # 逐个取出 单词列表 的元素（单词）
        if word[0].isdigit():  # 若 单词[0].isdigit(
            num = int(word)  # 把 int(单词) 存入 num
            if num <= prev:  # 若 num 不超过 前一个
                return False  # 返回 False
            prev = num  # 把 num 存入 前一个
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(areNumbersAscending("abc"))  # 打印输出
