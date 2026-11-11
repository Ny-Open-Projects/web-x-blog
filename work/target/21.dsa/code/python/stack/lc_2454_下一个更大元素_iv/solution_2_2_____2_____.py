# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def secondGreaterElement(nums):  # 定义函数 secondGreaterElement（参数：数组）
    n = len(nums)  # 把 长度(数组) 存入 元素个数
    res = [-1] * n  # 把 [ 减 1] 乘 元素个数 存入 结果
    st1 = []  # 把 [] 存入 st1
    st2 = []  # 把 [] 存入 st2

    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        v = nums[i]  # 把 数组[下标 i] 存入 值

        # Find elements in st1 with second greater
        pos = len(st2) - 1  # 把 长度(st2) 减 1 存入 pos
        while pos >= 0 and st2[pos] < v:  # 循环，直到不满足「pos 不低于 0 and st2[pos] 小于 值」
            pos -= 1  # pos累减 1

        # Move elements from st2 to st1
        for j in range(pos + 1, len(st2)):  # 让 下标 j 从 pos 加 1 到 长度(st2 遍历
            res[st2[j]] = v  # 把 值 写入 res[st2[j]]

        # Move elements from st1 to st2
        new_st2 = []  # 把 [] 存入 new_st2
        while st1 and nums[st1[-1]] < v:  # 循环，直到不满足「st1 and 数组[st1[ 减 1]] 小于 值」
            new_st2.append(st1.pop())  # 把 st1 弹出 追加到列表尾部

        st2.extend(new_st2)  # st2.extend(new_st2)
        st1.append(i)  # 把 下标 i 追加到列表尾部

    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(secondGreaterElement([1, 2, 3]))  # 打印输出
