# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083565
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def binaryTreePaths(root):  # 定义函数 binaryTreePaths（参数：根节点）
    paths = []  # 把 [] 存入 paths
    if root == None:
        return paths  # 若 根节点 等于 None: return paths
    node_queue = [root]  # 把 [根节点] 存入 node_queue
    path_queue = [root.val.toString()]  # 把 [根节点.值.toString()] 存入 path_queue
    while len(node_queue):  # 循环，直到不满足「长度(node_queue」
        node = node_queue.pop(0)  # 把 node_queue 弹出 0) 存入 节点
        path = path_queue.pop(0)  # 把 path_queue 弹出 0) 存入 当前路径
        if node.left == None and node.right == None:  # 若 节点.左边界 等于 None and 节点.右边界 等于 None
            paths.append(path)  # 把 当前路径 追加到列表尾部
        else:  # 否则
            if node.left != None:  # 若 节点.左边界 不等于 None
                node_queue.append(node.left)  # 把 节点.左边界 追加到列表尾部
                path_queue.append(
                    path + "->" + node.left.val.toString()
                )  # 把 当前路径 加 「 减 超过 」 加 节点.左边界.值.toString( 追加到列表尾部
            if node.right != None:  # 若 节点.右边界 不等于 None
                node_queue.append(node.right)  # 把 节点.右边界 追加到列表尾部
                path_queue.append(
                    path + "->" + node.right.val.toString()
                )  # 把 当前路径 加 「 减 超过 」 加 节点.右边界.值.toString( 追加到列表尾部
    return paths  # 返回 paths


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(binaryTreePaths(None))  # 打印输出
