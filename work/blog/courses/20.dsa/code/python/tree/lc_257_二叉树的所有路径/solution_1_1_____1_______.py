# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083565
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def binaryTreePaths(root):  # 定义函数 binaryTreePaths（参数：根节点）
    paths = []  # 把 [] 存入 paths

    def construct_paths(root, path):  # 定义函数 construct_paths（参数：根节点, 当前路径）
        if root:  # 若 根节点
            path += root.val.toString()  # 当前路径累加 根节点.值.toString()
            if (
                root.left == None and root.right == None
            ):  # 若 根节点.左边界 等于 None and 根节点.右边界 等于 None
                paths.append(path)  # 把 当前路径 追加到列表尾部
            else:  # 否则
                path += "->"  # 当前路径累加 「 减 超过 」
                construct_paths(root.left, path)  # construct_paths(根节点.左边界, 当前路径)
                construct_paths(root.right, path)  # construct_paths(根节点.右边界, 当前路径)

    construct_paths(root, "")  # construct_paths(根节点, 「」)
    return paths  # 返回 paths


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(binaryTreePaths(None))  # 打印输出
