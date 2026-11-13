# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def letterCombinations(digits):  # 定义函数 letterCombinations（参数：digits）
    if not digits:  # 若 not digits
        return []  # 返回 []
    mapping = {  # 把 { 存入 mapping
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",  # '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    combos = [""]  # 把 [''] 存入 combos
    for d in digits:  # 逐个取出 digits 的元素（d）
        combos = [
            p + c for p in combos for c in mapping[d]
        ]  # 把 [节点 加 字符 for 节点 in combos for 字符 in mapping[d]] 存入 combos
    return combos  # 返回 combos


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(letterCombinations("23"))  # 打印输出
