# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def frequencySort(s):  # 定义函数 frequencySort（参数：字符串）
    mp = {}  # 把 {} 存入 mp
    for ch in s:  # 逐个取出 字符串 的元素（字符）
        mp[ch] = mp.get(ch, 0) + 1  # 把 mp 查找 字符, 0) 加 1 写入 mp[ch]
    arr = sorted(
        mp.items(), key=lambda x: -x[1]
    )  # 把 sorted(mp.items(), key 赋值为 lambda x: 减 x[1]) 存入 数组
    result = ""  # 把 '' 存入 结果
    for ch, cnt in arr:  # for 字符, 计数 in 数组:
        result += ch * cnt  # 结果累加 字符 乘 计数
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(frequencySort("tree"))  # 打印输出
