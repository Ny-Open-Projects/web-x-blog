# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240399
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def partition(s):  # 定义函数 partition（参数：字符串）
    result = []  # 把 [] 存入 结果

    def backtrack(start, path):  # 定义函数 backtrack（参数：起点, 当前路径）
        if start == len(s):  # 若 起点 等于 长度(字符串
            result.append(path[:])  # 把 复制 当前路径 追加到列表尾部
            return  # return
        for end in range(start + 1, len(s) + 1):  # 让 终点 从 起点 加 1 到 长度(字符串 遍历
            if s[start:end] == s[start:end][::-1]:  # 若 字符串[起点:终点] 等于 字符串[起点:终点][:: 减 1]
                path.append(s[start:end])  # 把 字符串[起点:终点] 追加到列表尾部
                backtrack(end, path)  # backtrack(终点, 当前路径)
                path.pop()  # 弹出栈顶元素

    backtrack(0, [])  # backtrack(0, [])
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(partition("abc"))  # 打印输出
