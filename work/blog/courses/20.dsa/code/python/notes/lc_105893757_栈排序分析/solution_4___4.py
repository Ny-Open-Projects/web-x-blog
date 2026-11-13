# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_min(stack):  # 定义函数 get_min（参数：栈）
    """弹出栈中所有元素并找出其中最小值，其余元素压回（栈中移除一个最小值）。"""
    if len(stack) == 1:  # 若 长度(栈) 等于 1
        return stack.pop()  # 返回 栈 弹出 )
    top = stack.pop()  # 把 栈 弹出 ) 存入 top
    rest_min = get_min(stack)  # 把 get_min(栈) 存入 rest_min
    if top < rest_min:  # 若 top 小于 rest_min
        stack.append(rest_min)  # 把 rest_min 追加到列表尾部
        return top  # 返回 top
    else:  # 否则
        stack.append(top)  # 把 top 追加到列表尾部
        return rest_min  # 返回 rest_min


def sort_stack_min(stack):  # 定义函数 sort_stack_min（参数：栈）
    """用“反复取最小值”的方式对栈排序（选择排序思想），得到升序列表。"""
    res = []  # 把 [] 存入 结果
    while stack:  # 循环，直到不满足「栈」
        res.append(get_min(stack))  # 把 get_min(栈 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = [3, 1, 4, 2]  # 把 [3, 1, 4, 2] 存入 字符串
    print("排序结果(升序):", sort_stack_min(s))  # 打印输出
