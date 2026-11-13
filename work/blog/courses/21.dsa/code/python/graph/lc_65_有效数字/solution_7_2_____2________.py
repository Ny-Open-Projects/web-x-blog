# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isNumber(s):  # 定义函数 isNumber（参数：字符串）
    graph = {  # 把 { 存入 graph
        0: {"blank": 0, "sign": 1, ".": 2, "digit": 6},
        1: {"digit": 6, ".": 2},
        2: {"digit": 3},
        3: {"digit": 3, "e": 4},
        4: {"digit": 5, "sign": 7},
        5: {"digit": 5},
        6: {"digit": 6, ".": 3, "e": 4},
        7: {"digit": 5},
    }
    state = 0  # 把 0 存入 state
    for ch in s.strip():  # 逐个取出 字符串 的元素（字符）
        if "0" <= ch <= "9":  # 若 '0' 不超过 字符 不超过 '9'
            c = "digit"  # 把 'digit' 存入 字符
        elif ch == " ":  # 否则，若 字符 等于 ' '
            c = "blank"  # 把 'blank' 存入 字符
        elif ch in "+-":  # 否则，若 字符 in ' 加 减 '
            c = "sign"  # 把 'sign' 存入 字符
        else:  # 否则
            c = ch.lower()  # 把 字符.lower() 存入 字符
        if c not in graph[state]:  # 若 字符 not in graph[state]
            return False  # 返回 False
        state = graph[state][c]  # 把 graph[state][字符] 存入 state
    return state in (3, 5, 6)  # 返回 state in (3, 5, 6)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isNumber("0"))  # 打印输出
    print(isNumber("abc"))  # 打印输出
