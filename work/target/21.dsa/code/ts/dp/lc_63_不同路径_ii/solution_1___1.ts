// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130713079
/**
 ** LeetCode 63. 不同路径 II
 ** 方案：方案1（二维 DP）
 ** 来源：python 参考忠实移植
 */

function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  // 定义函数/方法 uniquePathsWithObstacles
  const m = obstacleGrid.length; // 把 obstacleGrid.长度 存入 映射表
  const n = obstacleGrid[0].length; // 把 obstacleGrid[0].长度 存入 元素个数
  const dp: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));
  for (let i = 0; i < m; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    if (obstacleGrid[i][0] === 0)
      dp[i][0] = 1; // 若 obstacleGrid[下标 i][0] 全等于 0) DP 表[下标 i][0] 赋值为 1;
    else break; // 否则
  }
  for (let j = 0; j < n; j++) {
    // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
    if (obstacleGrid[0][j] === 0)
      dp[0][j] = 1; // 若 obstacleGrid[0][下标 j] 全等于 0) DP 表[0][下标 j] 赋值为 1;
    else break; // 否则
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
  const cases: { in: number[][]; want: number }[] = [
    {
      in: [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
      ],
      want: 2,
    },
    {
      in: [
        [0, 0],
        [1, 0],
      ],
      want: 1,
    },
    {
      in: [
        [0, 1],
        [0, 0],
      ],
      want: 1,
    },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = uniquePathsWithObstacles(c.in); // 把 uniquePathsWithObstacles(字符.in) 存入 got
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
