# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
# 顺序查找 - 带测试用例版本
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def seq_search(nums, target):  # 定义函数 seq_search（参数：数组, 目标值）
    for i in range(len(nums)):  # 让 下标 i 从 长度(数组 遍历
        if nums[i] == target:  # 若 数组[下标 i] 等于 目标值
            return i  # 返回 下标 i
    return -1  # 返回 减 1


def test_seq_search():  # 定义函数 test_seq_search（参数：无）
    test_cases = [
        ([15, 4, 23, 52, 1], 23, 2),
        ([15, 4, 23, 52, 1], 123, -1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, -1),
        ([10, 20, 30, 40, 50], 10, 0),
        ([10, 20, 30, 40, 50], 50, 4),
        ([], 1, -1),
        ([1], 1, 0),
        ([1], 2, -1),
    ]
    for i, (nums, target, expected) in enumerate(
        test_cases
    ):  # for 下标 i, (数组, 目标值, expected) in enumerate(test_cases):
        result = seq_search(nums, target)  # 把 seq_search(数组, 目标值) 存入 结果
        status = (
            "PASS" if result == expected else "FAIL"
        )  # 把 'PASS' if 结果 等于 expected else 'FAIL' 存入 status
        print(f"Test Case {i + 1}: {status} (expected {expected}, got {result})")  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    test_seq_search()  # test_seq_search()
