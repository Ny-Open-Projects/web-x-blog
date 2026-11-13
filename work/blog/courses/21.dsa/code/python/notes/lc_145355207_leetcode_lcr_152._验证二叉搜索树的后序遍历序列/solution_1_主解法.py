# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def verify_postorder(postorder):  # 定义函数 verify_postorder（参数：postorder）
    # 验证给定序列是否为某二叉搜索树的后序遍历结果
    def helper(seq):  # 定义函数 helper（参数：seq）
        if len(seq) <= 1:  # 若 长度(seq) 不超过 1
            return True  # 返回 True
        root = seq[-1]  # 把 seq[ 减 1] 存入 根节点
        # 左子树：所有小于根
        i = 0  # 把 0 存入 下标 i
        while (
            i < len(seq) - 1 and seq[i] < root
        ):  # 循环，直到不满足「下标 i 小于 长度(seq) 减 1 and seq[下标 i] 小于 根节点」
            i += 1  # 下标 i累加 1
        # 右子树：必须全部大于根
        for j in range(i, len(seq) - 1):  # 让 下标 j 从 下标 i 到 长度(seq 遍历
            if seq[j] <= root:  # 若 seq[下标 j] 不超过 根节点
                return False  # 返回 False
        return helper(seq[:i]) and helper(
            seq[i:-1]
        )  # 返回 helper(seq[:下标 i]) and helper(seq[下标 i: 减 1])

    return helper(postorder)  # 返回 helper(postorder)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(verify_postorder([1, 6, 3, 2, 5]))  # False
    print(verify_postorder([1, 3, 2, 6, 5]))  # True
    print(verify_postorder([4, 8, 6, 12, 10, 9]))  # True
