# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def solve_crime():  # 定义函数 solve_crime（参数：无）
    # 刑侦案件：六嫌疑人 A,B,C,D,E,F，1 表示作案，0 表示未作案
    # 线索：
    # 1) A、B 至少有一人作案            -> a or b
    # 2) A、E、F 至少两人参与          -> (a&e)|(a&f)|(e&f)
    # 3) A、D 不可能是同案犯            -> not (a and d)
    # 4) B、C 或同时作案或与本案无关    -> (b&c)|(~b&~c)
    # 5) C、D 中有且仅有一人作案        -> (c&~d)|(~c&d)
    # 6) 若 D 没作案则 E 也不可能作案   -> d or (~d and ~e)
    found = False  # 把 False 存入 found
    for a in range(2):  # 让 数组 从 2 遍历
        for b in range(2):  # 让 b 从 2 遍历
            for c in range(2):  # 让 字符 从 2 遍历
                for d in range(2):  # 让 d 从 2 遍历
                    for e in range(2):  # 让 e 从 2 遍历
                        for f in range(2):  # 让 f 从 2 遍历
                            if (
                                (a or b)  # 若 (数组 or b) and
                                and (
                                    (a and e) or (a and f) or (e and f)
                                )  # ((数组 and e) or (数组 and f) or (e and f)) and
                                and (not (a and d))  # (not (数组 and d)) and
                                and (
                                    (b and c) or (not b and not c)
                                )  # ((b and 字符) or (not b and not 字符)) and
                                and (
                                    (c and not d) or (not c and d)
                                )  # ((字符 and not d) or (not 字符 and d)) and
                                and (d or (not d and not e))
                            ):  # (d or (not d and not e))):
                                people = "".join(
                                    name
                                    for name, v in zip("ABCDEF", [a, b, c, d, e, f])
                                    if v  # name for name, 值 in zip('ABCDEF', [数组, b, 字符, d, e, f]) if 值
                                )
                                print("作案人员有：", people)  # 打印输出
                                found = True  # 把 True 存入 found
    if not found:  # 若 not found
        print("未找到作案人员!")  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    solve_crime()  # solve_crime()
