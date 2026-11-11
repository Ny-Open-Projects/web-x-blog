// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853278
/**
 ** LeetCode 583. 两个字符串的删除操作
 ** 方案：方案1（最长公共子序列 LCS -> m + n - 2*lcs）
 ** 来源：python 参考忠实移植
 */

function minDistance(word1: string, word2: string): number {
  // 定义函数/方法 minDistance
  const m = word1.length; // 把 word1.长度 存入 映射表
  const n = word2.length; // 把 word2.长度 存入 元素个数
  const dp: number[][] = Array.from({ length: m + 1 }, () =>
    new Array(n + 1).fill(0),
  );
  for (let i = 1; i <= m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    const c1 = word1[i - 1]; // 把 word1[下标 i 减 1] 存入 c1
    for (let j = 1; j <= n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
      const c2 = word2[j - 1]; // 把 word2[下标 j 减 1] 存入 c2
      if (c1 === c2) dp[i][j] = dp[i - 1][j - 1] + 1;
      else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); // 否则
    }
  }
  const lcs = dp[m][n]; // 把 DP 表[映射表][元素个数] 存入 lcs
  return m - lcs + n - lcs; // 返回 映射表 减 lcs 加 元素个数 减 lcs
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { in: [string, string]; want: number }[] = [
    { in: ['sea', 'eat'], want: 2 },
    { in: ['', 'abc'], want: 3 },
    { in: ['a', 'b'], want: 2 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = minDistance(c.in[0], c.in[1]); // 把 minDistance(字符.in[0], 字符.in[1]) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL', JSON.stringify(c.in), 'want', c.want, 'got', got); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
