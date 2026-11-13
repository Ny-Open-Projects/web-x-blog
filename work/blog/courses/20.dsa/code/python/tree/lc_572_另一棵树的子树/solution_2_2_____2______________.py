# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089820
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getMaxElement(root, maxElement):  # 定义函数 getMaxElement（参数：根节点, maxElement）
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getMaxElement(None, None))  # 打印输出
