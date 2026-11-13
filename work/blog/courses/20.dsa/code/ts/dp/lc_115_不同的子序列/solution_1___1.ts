// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function numDistinct(s: string, t: string): number {
  // 定义函数/方法 numDistinct
  const m = s.length,
    n = t.length; // 把 字符串.长度, 元素个数 赋值为 另一字符串.长度 存入 映射表
  const dp: number[][] = Array.from({ length: m + 1 }, () =>
    new Array(n + 1).fill(0),
  );
  for (let i = 0; i <= m; i++) dp[i][n] = 1; // 让 下标 i 从 0 开始计数，下标 i 不超过 映射表 就继续
  for (let i = m - 1; i >= 0; i--) {
    // 让 下标 i 从 映射表 减 1 开始计数，下标 i 不低于 0 就继续
    for (let j = n - 1; j >= 0; j--) {
      // 让 下标 j 从 元素个数 减 1 开始计数，下标 j 不低于 0 就继续
      if (s[i] === t[j]) dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j];
      else dp[i][j] = dp[i + 1][j]; // 否则
    }
  }
  return dp[0][0]; // 返回 DP 表[0][0]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(numDistinct('rabbbit', 'rabbit'), 3, 'nd1'); // 断言校验
  assertEq(numDistinct('babgbag', 'bag'), 5, 'nd2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
