# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def letterCombinations(digits):  # 定义函数 letterCombinations（参数：digits）
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
    res = []  # 把 [] 存入 结果

    def backtrack(path, index):  # 定义函数 backtrack（参数：当前路径, index）
        if index == len(digits):  # 若 index 等于 长度(digits
            res.append("".join(path))  # 把 ''.join(当前路径 追加到列表尾部
            return  # return
        for ch in mapping[digits[index]]:  # 逐个取出 mapping 的元素（字符）
            path.append(ch)  # 把 字符 追加到列表尾部
            backtrack(path, index + 1)  # backtrack(当前路径, index 加 1)
            path.pop()  # 弹出栈顶元素

    if digits:  # 若 digits
        backtrack([], 0)  # backtrack([], 0)
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(letterCombinations("23"))  # 打印输出
