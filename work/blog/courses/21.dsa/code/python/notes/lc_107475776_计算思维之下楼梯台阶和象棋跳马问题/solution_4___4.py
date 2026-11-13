# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def horse_jump_count():  # 定义函数 horse_jump_count（参数：无）
    # 象棋跳马问题（方案4）：使用平行数组 dx/dy 描述四种马步
    dx = [1, 2, 2, 1]  # 把 [1, 2, 2, 1] 存入 dx
    dy = [2, 1, -1, -2]  # 把 [2, 1, 减 1, 减 2] 存入 dy
    count = 0  # 把 0 存入 计数

    def jump(x, y):  # 定义函数 jump（参数：x, y）
        nonlocal count  # nonlocal 计数
        if x == 8 and y == 4:  # 若 x 等于 8 and y 等于 4
            count += 1  # 计数累加 1
            return  # return
        for k in range(4):  # 让 下标 k 从 4 遍历
            x1, y1 = x + dx[k], y + dy[k]  # 把 x 加 dx[下标 k], y 加 dy[下标 k] 写入 x1, y1
            if x1 < 0 or x1 > 8 or y1 < 0 or y1 > 4:  # 若 x1 小于 0 or x1 超过 8 or y1 小于 0 or y1 超过 4
                continue  # 跳过本轮，进入下一次
            jump(x1, y1)  # jump(x1, y1)

    jump(0, 0)  # jump(0, 0)
    return count  # 返回 计数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print("跳马方案总数(0,0)->(8,4):", horse_jump_count())  # 打印输出
