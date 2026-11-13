# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def count_binary_substrings3(s):  # 定义函数 count_binary_substrings3（参数：字符串）
    prev, cur, ans = 0, 1, 0  # 上一组、当前组、答案
    for i in range(1, len(s)):  # 从下标 1 扫描到末尾
        if s[i] == s[i - 1]:  # 同组
            cur += 1
        else:  # 换组
            ans += min(prev, cur)  # 结算上一对相邻组
            prev, cur = cur, 1
    return ans + min(prev, cur)  # 结算最后一对


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = {"00110011": 6, "10101": 4, "0": 0, "111000": 3}
    ok = True
    for s, want in cases.items():
        got = count_binary_substrings3(s)
        if got != want:
            ok = False
            print("FAIL", s, got, "want", want)
    print("PASS" if ok else "FAILED")
