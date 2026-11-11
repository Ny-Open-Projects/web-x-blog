# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sort_stack_recursive(stack):  # 定义函数 sort_stack_recursive（参数：栈）
    """用递归对栈排序（栈底最小，栈顶最大）：弹出栈顶后先递归排序剩余部分，再有序插入。"""
    if stack:  # 若 栈
        top = stack.pop()  # 把 栈 弹出 ) 存入 top
        sort_stack_recursive(stack)  # sort_stack_recursive(栈)
        sorted_insert(stack, top)  # sorted_insert(栈, top)
    return stack  # 返回 栈


def sorted_insert(stack, val):  # 定义函数 sorted_insert（参数：栈, 值）
    if not stack or val > stack[-1]:  # 若 not 栈 or 值 超过 栈[ 减 1]
        stack.append(val)  # 把 值 追加到列表尾部
    else:  # 否则
        tmp = stack.pop()  # 把 栈 弹出 ) 存入 临时变量
        sorted_insert(stack, val)  # sorted_insert(栈, 值)
        stack.append(tmp)  # 把 临时变量 追加到列表尾部


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = [1, 3, 2, 4]  # 把 [1, 3, 2, 4] 存入 字符串
    print("排序结果(栈顶最大):", sort_stack_recursive(s))  # 打印输出
