# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001
# 根据字符出现频率排序 - 方案: 桶排序
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def frequency_sort(s):  # 定义函数 frequency_sort（参数：字符串）
    cnt = {}  # 把 {} 存入 计数
    for ch in s:  # 逐个取出 字符串 的元素（字符）
        cnt[ch] = cnt.get(ch, 0) + 1  # 把 计数 查找 字符, 0) 加 1 写入 cnt[ch]
    max_freq = max(cnt.values()) if cnt else 0  # 把 取较大值 计数.values()) if 计数 else 0 存入 max_freq
    buckets = [[] for _ in range(max_freq + 1)]  # 把 [[] for _ in range(max_freq 加 1)] 存入 buckets
    for ch, f in cnt.items():  # for 字符, f in 计数.items():
        buckets[f].append(ch)  # 把 字符 追加到列表尾部
    result = ""  # 把 '' 存入 结果
    for f in range(max_freq, 0, -1):  # 让 f 从 max_freq 倒数回去（每步减 1）
        for ch in buckets[f]:  # 逐个取出 buckets 的元素（字符）
            result += ch * f  # 结果累加 字符 乘 f
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(frequency_sort("tree"))  # 'eert' 或 'eetr'
