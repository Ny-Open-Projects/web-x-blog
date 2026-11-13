# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
import sys  # 提高递归深度上限（深输入防 RecursionError）
sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
def func(n):
 if n <= 1: return n
 return func(n-1) + func(n-1)