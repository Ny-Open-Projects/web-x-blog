# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753362
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def postorderTraversal(root):  # 定义函数 postorderTraversal（参数：根节点）
    result = []  # 把 [] 存入 结果

    def isValid(val):  # 定义函数 isValid（参数：值）
        val != None  # 把 None 写入 val !

        def postorderHandler(root):  # 定义函数 postorderHandler（参数：根节点）
            if not root:
                return result  # 若 not 根节点: return 结果
            isValid(root.left) and postorderHandler(
                root.left
            )  # isValid(根节点.左边界) and postorderHandler(根节点.左边界)
            isValid(root.right) and postorderHandler(
                root.right
            )  # isValid(根节点.右边界) and postorderHandler(根节点.右边界)
            isValid(root.val) and result.append(root.val)  # 把 根节点.值 追加到列表尾部
            return result  # 返回 结果

        return postorderHandler(root)  # 返回 postorderHandler(根节点)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(postorderTraversal(None))  # 打印输出
