# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
def lcs(text1, text2):
    """最长公共子序列（LCS）动态规划。返回长度与具体子序列。"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # 回溯构造子序列
    i, j = m, n
    seq = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            seq.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    seq.reverse()
    return dp[m][n], ''.join(seq)


if __name__ == '__main__':
    length, seq = lcs("abcde", "ace")
    print("LCS 长度:", length, "子序列:", seq)  # 3 ace
