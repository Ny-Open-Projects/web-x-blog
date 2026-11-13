# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def restoreIpAddresses(s):  # 定义函数 restoreIpAddresses（参数：字符串）
    res = []  # 把 [] 存入 结果

    def backtrack(start, path):  # 定义函数 backtrack（参数：起点, 当前路径）
        if len(path) == 4:  # 若 长度(当前路径) 等于 4
            if start == len(s):  # 若 起点 等于 长度(字符串
                res.append(".".join(path))  # 把 '.'.join(当前路径 追加到列表尾部
            return  # return
        for length in range(1, 4):  # 让 长度 从 1 到 4 遍历
            if start + length > len(s):  # 若 起点 加 长度 超过 长度(字符串
                break  # 跳出循环
            segment = s[start : start + length]  # 把 字符串[起点:起点 加 长度] 存入 segment
            if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                continue  # 跳过本轮，进入下一次
            backtrack(start + length, path + [segment])  # backtrack(起点 加 长度, 当前路径 加 [segment])

    backtrack(0, [])  # backtrack(0, [])
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(restoreIpAddresses("101023"))  # 打印输出
