# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def letterCombinations(digits):  # 定义函数 letterCombinations（参数：digits）
    if not digits:  # 若 not digits
        return []  # 返回 []
    d = {  # 把 { 存入 d
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = [""]  # 把 [''] 存入 结果
    for ch in digits:  # 逐个取出 digits 的元素（字符）
        if ch not in d:  # 若 字符 not in d
            continue  # 跳过本轮，进入下一次
        res = [
            p + c for p in res for c in d[ch]
        ]  # 把 [节点 加 字符 for 节点 in 结果 for 字符 in d[字符]] 存入 结果
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(letterCombinations("23"))  # 打印输出
    print(letterCombinations(""))  # 打印输出
    print(letterCombinations("2"))  # 打印输出
