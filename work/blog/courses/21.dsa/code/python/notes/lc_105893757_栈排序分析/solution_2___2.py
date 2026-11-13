# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sort_stack_two_stacks(stack):  # 定义函数 sort_stack_two_stacks（参数：栈）
    """用两个栈对栈排序（升序，栈顶最大）：
    主栈逐个弹出，借助辅助栈把所有比当前元素大的都压回主栈，再把当前元素压入辅助栈。"""
    aux = []  # 把 [] 存入 aux
    while stack:  # 循环，直到不满足「栈」
        top = stack.pop()  # 把 栈 弹出 ) 存入 top
        while aux and aux[-1] > top:  # 循环，直到不满足「aux and aux[ 减 1] 超过 top」
            stack.append(aux.pop())  # 把 aux 弹出 追加到列表尾部
        aux.append(top)  # 把 top 追加到列表尾部
    return aux  # 返回 aux


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = [1, 3, 2, 4]  # 把 [1, 3, 2, 4] 存入 字符串
    res = sort_stack_two_stacks(s)  # 把 sort_stack_two_stacks(字符串) 存入 结果
    print("排序结果(栈顶最大):", res)  # 打印输出
