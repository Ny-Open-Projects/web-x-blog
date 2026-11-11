# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def frequencySort(s):  # 定义函数 frequencySort（参数：字符串）
    map = {}  # 把 {} 存入 映射表
    for item in s:  # 逐个取出 字符串 的元素（item）
        map[item] = map.get(item, 0) + 1  # 把 映射表 查找 item, 0) 加 1 写入 map[item]
    arr = sorted(map.items(), key=lambda x: x[1], reverse=True)
    result = ""  # 把 '' 存入 结果
    for item in arr:  # 逐个取出 数组 的元素（item）
        result += item[0] * item[1]  # 结果累加 item[0] 乘 item[1]
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(frequencySort("abc"))  # 打印输出
