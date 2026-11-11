# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345560
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def flatArray(arr):  # 定义函数 flatArray（参数：数组）
    stack = list(arr)  # 把 列表(数组) 存入 栈
    ret = []  # 把 [] 存入 ret
    while stack:  # 循环，直到不满足「栈」
        next_item = stack.pop()  # 把 栈 弹出 ) 存入 next_item
        if isinstance(next_item, list):  # 若 isinstance(next_item, 列表
            stack.extend(next_item)  # 栈.extend(next_item)
        else:  # 否则
            ret.insert(0, next_item)  # ret 插入 0, next_item)
    return ret  # 返回 ret


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(flatArray([1, 2, 3]))  # 打印输出
