# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def count_sort(lst):  # 定义函数 count_sort（参数：lst）
    # 计数排序 - 优化版（按 max-min+1 缩小计数数组，返回新数组）
    length = len(lst)  # 把 长度(lst) 存入 长度
    if length < 2:  # 若 长度 小于 2
        return lst  # 返回 lst
    max_val = max(lst)  # 把 取较大值 lst) 存入 max_val
    min_val = min(lst)  # 把 取较小值 lst) 存入 min_val
    count_list = [0] * (max_val - min_val + 1)  # 把 [0] 乘 (max_val 减 min_val 加 1) 存入 count_list
    for num in lst:  # 逐个取出 lst 的元素（num）
        count_list[num - min_val] += 1  # 把 1 写入 count_list[num - min_val] +
    result = []  # 把 [] 存入 结果
    for j in range(max_val - min_val + 1):  # 让 下标 j 从 max_val 减 min_val 加 1 遍历
        if count_list[j] == 0:  # 若 count_list[下标 j] 等于 0
            continue  # 跳过本轮，进入下一次
        if count_list[j] > 1:  # 若 count_list[下标 j] 超过 1
            result.extend(
                [j + min_val] * count_list[j]
            )  # 结果.extend([下标 j 加 min_val] 乘 count_list[下标 j])
        else:  # 否则
            result.append(j + min_val)  # 把 下标 j 加 min_val 追加到列表尾部
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lst = [102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106, 109, 102]
    print(count_sort(lst))  # [101, 101, 102, ... , 109, 109]
