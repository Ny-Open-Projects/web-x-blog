// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829625
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function longestCommonSubsequence(text1: string, text2: string): number {
    // 定义函数/方法 longestCommonSubsequence
    const m = text1.length; // 把 text1.长度 存入 映射表
    const n = text2.length; // 把 text2.长度 存入 元素个数
    const dp: number[][] = Array.from({ length: m + 1 }, () =>
      new Array(n + 1).fill(0),
    );
    for (let i = 1; i <= m; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      const c1 = text1[i - 1]; // 把 text1[下标 i 减 1] 存入 c1
      for (let j = 1; j <= n; j++) {
        // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
        const c2 = text2[j - 1]; // 把 text2[下标 j 减 1] 存入 c2
        if (c1 === c2) {
          // 若 c1 全等于 c2
          dp[i][j] = dp[i - 1][j - 1] + 1; // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1; 写入 dp[i][j]
        } else {
          // 否则
          dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
      }
    }
    return dp[m][n]; // 返回 DP 表[映射表][元素个数]
  }

  const cases = [
    { t1: 'abcde', t2: 'ace', want: 3 },
    { t1: 'abc', t2: 'abc', want: 3 },
    { t1: 'abc', t2: 'def', want: 0 },
  ];

  let fail = false; // 把 false 存入 fail
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const c = cases[i]; // 把 cases[下标 i] 存入 字符
    const got = longestCommonSubsequence(c.t1, c.t2); // 把 longestCommonSubsequence(字符.t1, 字符.t2) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        `FAIL case${i} longestCommonSubsequence(${c.t1},${c.t2})=${got} want ${c.want}`,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
