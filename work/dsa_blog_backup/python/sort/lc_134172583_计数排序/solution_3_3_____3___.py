# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def count_sort(list):  # 定义函数 count_sort（参数：列表）
    length = len(list)  # 把 长度(列表) 存入 长度
    if length < 2:  # 若 长度 小于 2
        return list  # 返回 列表
    max_val = max(list)  # 把 取较大值 列表) 存入 max_val
    min_val = min(list)  # 把 取较小值 列表) 存入 min_val
    count_list = [0] * (max_val - min_val + 1)  # 把 [0] 乘 (max_val 减 min_val 加 1) 存入 count_list
    for num in list:  # 逐个取出 列表 的元素（num）
        count_list[num - min_val] += 1  # 把 1 写入 count_list[num - min_val] +
    str_result = ""  # 把 '' 存入 str_result
    for j in range(max_val - min_val + 1):  # 让 下标 j 从 max_val 减 min_val 加 1 遍历
        if count_list[j] == 0:  # 若 count_list[下标 j] 等于 0
            continue  # 跳过本轮，进入下一次
        if count_list[j] > 1:  # 若 count_list[下标 j] 超过 1
            str_result += (str(j + min_val) + ",") * count_list[j]
        else:  # 否则
            str_result += str(j + min_val) + ","  # str_result累加 str(下标 j 加 min_val) 加 ','
    str_result = str_result.rstrip(",")  # 把 str_result.rstrip(',') 存入 str_result
    result = [
        int(item) for item in str_result.split(",")
    ]  # 把 [int(item) for item in str_result.split(',')] 存入 结果
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(count_sort([4, 2, 2, 8, 3, 3, 1]))  # 打印输出
