# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def intersect(nums1, nums2):  # 定义函数 intersect（参数：数组1, 数组2）
    if len(nums1) > len(nums2):  # 若 长度(数组1) 超过 长度(数组2
        return intersect(nums2, nums1)  # 返回 intersect(数组2, 数组1)
    mp = {}  # 把 {} 存入 mp
    for num in nums1:  # 逐个取出 数组1 的元素（num）
        mp[num] = mp.get(num, 0) + 1  # 把 mp 查找 num, 0) 加 1 写入 mp[num]
    intersection = []  # 把 [] 存入 intersection
    for num in nums2:  # 逐个取出 数组2 的元素（num）
        if num in mp and mp[num] > 0:  # 若 num in mp and mp[num] 超过 0
            intersection.append(num)  # 把 num 追加到列表尾部
            mp[num] -= 1  # mp[num]累减 1
    return intersection  # 返回 intersection


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(intersect([1, 2, 2, 1], [2, 2]))  # 打印输出
