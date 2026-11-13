# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239508
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def combinationSum(candidates, target):  # 定义函数 combinationSum（参数：候选数组, 目标值）
    candidates.sort()  # 排序
    result = []  # 把 [] 存入 结果

    def backtrack(start, path, remaining):  # 定义函数 backtrack（参数：起点, 当前路径, remaining）
        if remaining == 0:  # 若 remaining 等于 0
            result.append(path[:])  # 把 复制 当前路径 追加到列表尾部
            return  # return
        for i in range(start, len(candidates)):  # 让 下标 i 从 起点 到 长度(候选数组 遍历
            if candidates[i] > remaining:  # 若 候选数组[下标 i] 超过 remaining
                break  # 跳出循环
            path.append(candidates[i])  # 把 候选数组[下标 i] 追加到列表尾部
            backtrack(
                i, path, remaining - candidates[i]
            )  # backtrack(下标 i, 当前路径, remaining 减 候选数组[下标 i])
            path.pop()  # 弹出栈顶元素

    backtrack(0, [], target)  # backtrack(0, [], 目标值)
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(combinationSum([2, 3, 6, 7], 7))  # 打印输出
