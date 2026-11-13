// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
// LeetCode 113951689. 动态规划之 LCS — TypeScript 版（最长公共子序列：DP 填表 + 回溯构造）

function lcsLength(a: string, b: string): number {
  // 定义函数/方法 lcsLength
  const m = a.length; // 把 数组.长度 存入 映射表
  const n = b.length; // 把 b.长度 存入 元素个数
  const dp: number[][] = Array.from({ length: m + 1 }, () =>
    new Array(n + 1).fill(0),
  );
  for (let i = 1; i <= m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (let j = 1; j <= n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
      if (a[i - 1] === b[j - 1]) {
        // 若 数组[下标 i 减 1] 全等于 b[下标 j 减 1]
        dp[i][j] = dp[i - 1][j - 1] + 1; // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1; 写入 dp[i][j]
      } else {
        // 否则
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[m][n]; // 返回 DP 表[映射表][元素个数]
}

function lcsString(a: string, b: string): string {
  // 定义函数/方法 lcsString
  const m = a.length; // 把 数组.长度 存入 映射表
  const n = b.length; // 把 b.长度 存入 元素个数
  const dp: number[][] = Array.from({ length: m + 1 }, () =>
    new Array(n + 1).fill(0),
  );
  for (let i = 1; i <= m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (let j = 1; j <= n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
      dp[i][j] =
        a[i - 1] === b[j - 1] // 把 数组[下标 i 减 1] 全等于 b[下标 j 减 1] 写入 dp[i][j]
          ? dp[i - 1][j - 1] + 1 // ? DP 表[下标 i 减 1][下标 j 减 1] 加 1
          : Math.max(dp[i - 1][j], dp[i][j - 1]); // : Math.取较大值 DP 表[下标 i 减 1][下标 j], DP 表[下标 i][下标 j 减 1]);
    }
  }
  // 回溯构造一条 LCS
  let out = ''; // 把 「」 存入 out
  let i = m,
    j = n; // 把 映射表, 下标 j 赋值为 元素个数 存入 下标 i
  while (i > 0 && j > 0) {
    // 循环，直到不满足「下标 i 超过 0 且 下标 j 超过 0」
    if (a[i - 1] === b[j - 1]) {
      // 若 数组[下标 i 减 1] 全等于 b[下标 j 减 1]
      out = a[i - 1] + out; // 把 数组[下标 i 减 1] 加 out 存入 out
      i--;
      j--; // 下标 i 减一 ; 下标 j 减一 ;
    } else if (dp[i - 1][j] >= dp[i][j - 1]) {
      // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
      i--; // 下标 i 减一
    } else {
      // 否则
      j--; // 下标 j 减一
    }
  }
  return out; // 返回 out
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { a: string; b: string; want: number }[] = [
    { a: 'ABCBDAB', b: 'BDCABA', want: 4 }, // 如 BDAB / BCAB / BCBA
    { a: 'AGGTAB', b: 'GXTXAYB', want: 4 }, // GTAB
    { a: 'abc', b: 'abc', want: 3 },
    { a: '', b: 'abc', want: 0 }, // 边界：空串
    { a: 'abc', b: 'xyz', want: 0 }, // 边界：无公共字符
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = lcsLength(c.a, c.b); // 把 lcsLength(字符.数组, 字符.b) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(`FAIL lcsLength(${c.a},${c.b})=${got} want ${c.want}`);
    }
  }
  // 构造一致性：回溯出的串长度 = dp 长度，且是两串的公共子序列
  const pair: [string, string][] = [
    ['ABCBDAB', 'BDCABA'],
    ['AGGTAB', 'GXTXAYB'],
  ];
  for (const [a, b] of pair) {
    // for (const [数组, b] of pair) {
    const s = lcsString(a, b); // 把 lcsString(数组, b) 存入 字符串
    if (s.length !== lcsLength(a, b)) {
      fail = true;
      console.log('FAIL lcsString length', s);
    }
    let ia = 0,
      ib = 0; // 把 0, ib 赋值为 0 存入 ia
    for (const ch of s) {
      // for (const 字符 of 字符串) {
      while (ia < a.length && a[ia] !== ch) ia++; // 循环，直到不满足「ia 小于 数组.长度 且 数组[ia] 不等于 字符) ia 加一 ;」
      while (ib < b.length && b[ib] !== ch) ib++; // 循环，直到不满足「ib 小于 b.长度 且 b[ib] 不等于 字符) ib 加一 ;」
      if (ia >= a.length || ib >= b.length) {
        fail = true;
        console.log('FAIL not subsequence', s);
      }
      ia++;
      ib++; // ia 加一 ; ib 加一 ;
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
