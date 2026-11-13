# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hanoi(n, src, aux, dst, moves=None):  # 定义函数 hanoi（参数：元素个数, src, aux, dst, moves 赋值为 None）
    # 汉诺塔：递归解法，时间复杂度 O(2^n)
    if moves is None:  # 若 moves is None
        moves = []  # 把 [] 存入 moves
    if n == 1:  # 若 元素个数 等于 1
        moves.append((src, dst))  # 把 (src, dst 追加到列表尾部
        return moves  # 返回 moves
    hanoi(n - 1, src, dst, aux, moves)  # hanoi(元素个数 减 1, src, dst, aux, moves)
    moves.append((src, dst))  # 把 (src, dst 追加到列表尾部
    hanoi(n - 1, aux, src, dst, moves)  # hanoi(元素个数 减 1, aux, src, dst, moves)
    return moves  # 返回 moves


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    moves = hanoi(3, "A", "B", "C")  # 把 hanoi(3, 'A', 'B', 'C') 存入 moves
    print(len(moves), moves)  # 7 [(A,C),(A,B),...]
