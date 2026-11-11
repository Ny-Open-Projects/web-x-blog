# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244562
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque


def predictPartyVictory(senate):  # 定义函数 predictPartyVictory（参数：senate）
    # 贪心 + 循环队列：把两党的索引分别入队，谁先轮到就 ban 对方最靠前的议员，
    # 自己则排到队尾（索引 +n）进入下一轮，直到某一党为空
    n = len(senate)  # 把 长度(senate) 存入 元素个数
    radiant = deque()  # 把 deque() 存入 radiant
    dire = deque()  # 把 deque() 存入 dire
    for i, ch in enumerate(senate):  # 同时取 下标 i 与 字符 遍历
        if ch == "R":  # 若 字符 等于 'R'
            radiant.append(i)  # 把 下标 i 追加到列表尾部
        else:  # 否则
            dire.append(i)  # 把 下标 i 追加到列表尾部
    while radiant and dire:  # 循环，直到不满足「radiant and dire」
        if radiant[0] < dire[0]:  # 若 radiant[0] 小于 dire[0]
            radiant.append(radiant[0] + n)  # 把 radiant[0] 加 元素个数 追加到列表尾部
        else:  # 否则
            dire.append(dire[0] + n)  # 把 dire[0] 加 元素个数 追加到列表尾部
        radiant.popleft()  # radiant.popleft()
        dire.popleft()  # dire.popleft()
    return "Radiant" if radiant else "Dire"  # 返回 「Radiant」 if radiant else 「Radiant」


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(predictPartyVictory("RD"))  # 打印输出
    print(predictPartyVictory("RRRDDD"))  # 打印输出
    print(predictPartyVictory("DDR"))  # 打印输出
