# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def restore_ip_addresses(s):  # 定义函数 restore_ip_addresses（参数：字符串）
    res = []  # 结果集
    segs = []  # 当前段

    def valid(t):  # 段合法性：0 到 255 且无前导零
        return t.isdigit() and len(t) <= 3 and not (len(t) > 1 and t[0] == "0") and int(t) <= 255

    def dfs(start):  # 回溯：从 start 切下一段
        if len(segs) == 4:  # 已切满 4 段
            if start == len(s):  # 恰好用完字符串才收答案
                res.append(".".join(segs))
            return
        for l in range(1, 4):  # 每段取 1 到 3 个字符
            if start + l > len(s):
                break
            t = s[start : start + l]
            if not valid(t):
                continue
            segs.append(t)
            dfs(start + l)
            segs.pop()

    dfs(0)
    return res


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [("25525511135", ["255.255.11.135", "255.255.111.35"]), ("0000", ["0.0.0.0"]), ("abc", [])]
    ok = True
    for s, want in cases:
        got = sorted(restore_ip_addresses(s))
        if got != sorted(want):
            ok = False
            print("FAIL", s, got, "want", want)
    print("PASS" if ok else "FAILED")
