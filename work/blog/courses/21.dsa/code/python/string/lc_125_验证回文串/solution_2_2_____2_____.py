# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114949
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isPalindrome(s):  # 定义函数 isPalindrome（参数：字符串）
    left, right = 0, len(s) - 1  # 把 0, 长度(字符串) 减 1 写入 left, right
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        while (
            left < right and not s[left].isalnum()
        ):  # 循环，直到不满足「左边界 小于 右边界 and not 字符串[左边界].isalnum(」
            left += 1  # 左边界累加 1
        while (
            left < right and not s[right].isalnum()
        ):  # 循环，直到不满足「左边界 小于 右边界 and not 字符串[右边界].isalnum(」
            right -= 1  # 右边界累减 1
        if s[left].lower() != s[right].lower():  # 若 字符串[左边界].lower() 不等于 字符串[右边界].lower(
            return False  # 返回 False
        left += 1  # 左边界累加 1
        right -= 1  # 右边界累减 1
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isPalindrome("abc"))  # 打印输出
