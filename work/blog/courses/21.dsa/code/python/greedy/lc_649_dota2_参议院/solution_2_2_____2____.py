# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244562
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque


def predictPartyVictory(senate):  # 定义函数 predictPartyVictory（参数：senate）
    # 栈模拟：相同政党则入栈存活；不同则当前议员 ban 掉栈顶对手（栈顶重新入队等待后续轮次）
    queue = deque(senate)  # 把 deque(senate) 存入 队列
    stack = []  # 把 [] 存入 栈
    while queue:  # 循环，直到不满足「队列」
        s = queue.popleft()  # 把 队列.popleft() 存入 字符串
        if not stack or stack[-1] == s:  # 若 not 栈 or 栈[ 减 1] 等于 字符串
            stack.append(s)  # 把 字符串 追加到列表尾部
        else:  # 否则
            queue.append(stack.pop())  # 把 栈 弹出 追加到列表尾部
    return (
        "Radiant" if stack[-1] == "R" else "Dire"
    )  # 返回 「Radiant」 if 栈[ 减 1] 等于 'R' else 「Radiant」


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(predictPartyVictory("RD"))  # 打印输出
    print(predictPartyVictory("RRRDDD"))  # 打印输出
    print(predictPartyVictory("DDR"))  # 打印输出
