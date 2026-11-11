/**
 * LeetCode 877. 石子游戏
 * 方案：1 ) 方案1：动态规划
 * 来源：https://blog.csdn.net/tyro_java/article/details/145355902
 * 忠实翻译 python/dp/lc_877_石子游戏/solution_1_1_____1_____.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function stoneGame(piles: number[]): boolean {
    // 定义函数/方法 stoneGame
    const n = piles.length; // 把 piles.长度 存入 元素个数
    const dp: number[][] = Array.from({ length: n }, () =>
      new Array(n).fill(0),
    );
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      dp[i][i] = piles[i]; // 把 piles[下标 i]; 写入 dp[i][i]
    }
    for (let length = 2; length <= n; length++) {
      // 让 长度 从 2 开始计数，长度 不超过 元素个数 就继续
      for (let i = 0; i < n - length + 1; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 长度 加 1 就继续
        const j = i + length - 1; // 把 下标 i 加 长度 减 1 存入 下标 j
        dp[i][j] = Math.max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
      }
    }
    return dp[0][n - 1] > 0; // 返回 DP 表[0][元素个数 减 1] 超过 0
  }

  const cases: { in: number[]; want: boolean }[] = [
    { in: [5, 3, 4, 5], want: true },
    { in: [3, 7, 2, 3], want: true },
    { in: [1, 2], want: true },
    { in: [1], want: true },
    { in: [3, 4], want: true },
    { in: [0, 0], want: false },
    { in: [1, 100, 2], want: false },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = stoneGame(c.in); // 把 stoneGame(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL stoneGame(%o)=%s want %s', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
