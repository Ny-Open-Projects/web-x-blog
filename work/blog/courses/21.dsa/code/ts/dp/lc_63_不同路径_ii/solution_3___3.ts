// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130713079

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  // 定义函数/方法 uniquePathsWithObstacles
  const m = obstacleGrid.length; // 把 obstacleGrid.长度 存入 映射表
  const n = obstacleGrid[0].length; // 把 obstacleGrid[0].长度 存入 元素个数
  const dp: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));
  for (let i = 0; i < m; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    if (obstacleGrid[i][0] === 0) dp[i][0] = 1;
    else break;
  }
  for (let j = 0; j < n; j++) {
    // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
    if (obstacleGrid[0][j] === 0) dp[0][j] = 1;
    else break;
  }
  for (let i = 1; i < m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
    for (let j = 1; j < n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
      if (obstacleGrid[i][j] === 1) continue; // 若 obstacleGrid[下标 i][下标 j] 全等于 1) continue;
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]; // 把 DP 表[下标 i 减 1][下标 j] 加 DP 表[下标 i][下标 j 减 1]; 写入 dp[i][j]
    }
  }
  return dp[m - 1][n - 1]; // 返回 DP 表[映射表 减 1][元素个数 减 1]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    uniquePathsWithObstacles([
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0],
    ]),
    2,
    'case1',
  ); // 断言校验
  assertEq(
    uniquePathsWithObstacles([
      [0, 0],
      [1, 0],
    ]),
    1,
    'case2',
  ); // 断言校验
  assertEq(
    uniquePathsWithObstacles([
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1],
    ]),
    0,
    'case3',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
