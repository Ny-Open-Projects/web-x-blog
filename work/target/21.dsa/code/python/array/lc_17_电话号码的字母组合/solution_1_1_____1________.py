# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def letterCombinations(digits):  # 定义函数 letterCombinations（参数：digits）
    if len(digits) < 1:  # 若 长度(digits) 小于 1
        return []  # 返回 []
    dict_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    num = list(digits)  # 把 列表(digits) 存入 num
    code = []  # 把 [] 存入 code
    for item in num:  # 逐个取出 num 的元素（item）
        if item in dict_map:  # 若 item in dict_map
            code.append(dict_map[item])  # 把 dict_map[item] 追加到列表尾部

    def comb(arr):  # 定义函数 comb（参数：数组）
        if len(arr) == 1:  # 若 长度(数组) 等于 1
            return list(arr[0])  # 返回 列表(数组[0])
        tmp = []  # 把 [] 存入 临时变量
        for a in arr[0]:  # 逐个取出 数组 的元素（数组）
            for b in comb(arr[1:]):  # 逐个取出 comb 的元素（b）
                tmp.append(a + b)  # 把 数组 加 b 追加到列表尾部
        return tmp  # 返回 临时变量

    return comb(code)  # 返回 comb(code)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(letterCombinations("23"))  # 打印输出
