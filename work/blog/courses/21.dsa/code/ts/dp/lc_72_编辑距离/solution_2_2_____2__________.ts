// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848060

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function minDistance(word1: string, word2: string): number {
  // 定义函数/方法 minDistance
  const m = word1.length,
    n = word2.length; // 把 word1.长度, 元素个数 赋值为 word2.长度 存入 映射表
  const dp: number[][] = Array.from({ length: m + 1 }, () =>
    new Array(n + 1).fill(0),
  );
  for (let i = 0; i <= m; i++) dp[i][0] = i; // 让 下标 i 从 0 开始计数，下标 i 不超过 映射表 就继续
  for (let j = 0; j <= n; j++) dp[0][j] = j; // 让 下标 j 从 0 开始计数，下标 j 不超过 元素个数 就继续
  for (let i = 1; i <= m; i++)
    for (let j = 1; j <= n; j++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      if (word1[i - 1] === word2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
      else
        dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]); // 否则
    }
  return dp[m][n]; // 返回 DP 表[映射表][元素个数]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(minDistance('horse', 'ros'), 3, 'md'); // 断言校验
  assertEq(minDistance('', 'abc'), 3, 'empty1'); // 断言校验
  assertEq(minDistance('', ''), 0, 'empty'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
