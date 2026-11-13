# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130742026
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def preorderTraversal(root):  # 定义函数 preorderTraversal（参数：根节点）
    result = []  # 把 [] 存入 结果

    def isValid(val):  # 定义函数 isValid（参数：值）
        val != None  # 把 None 写入 val !

        def preorderHandler(root):  # 定义函数 preorderHandler（参数：根节点）
            if not root:
                return result  # 若 not 根节点: return 结果
            isValid(root.val) and result.append(root.val)  # 把 根节点.值 追加到列表尾部
            isValid(root.left) and preorderHandler(
                root.left
            )  # isValid(根节点.左边界) and preorderHandler(根节点.左边界)
            isValid(root.right) and preorderHandler(
                root.right
            )  # isValid(根节点.右边界) and preorderHandler(根节点.右边界)
            return result  # 返回 结果

        return preorderHandler(root)  # 返回 preorderHandler(根节点)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(preorderTraversal(None))  # 打印输出
