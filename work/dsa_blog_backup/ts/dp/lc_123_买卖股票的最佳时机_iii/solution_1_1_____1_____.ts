/**
 * LeetCode 123. 买卖股票的最佳时机 III
 * 方案：1 ) 方案1:动态规划
 * 来源：https://blog.csdn.net/tyro_java/article/details/144849793
 * 忠实翻译 python/dp/lc_123_买卖股票的最佳时机_iii/solution_1_1_____1_____.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maxProfit(prices: number[]): number {
    // 定义函数/方法 maxProfit
    // 动态规划空间降维
    const len = prices.length; // 把 价格序列.长度 存入 长度
    const dp: number[] = [0, 0, 0, 0, 0]; // 把 [0, 0, 0, 0, 0]; 写入 const dp: number[]
    dp[1] = -prices[0]; // 把 减 价格序列[0]; 写入 dp[1]
    dp[3] = -prices[0]; // 把 减 价格序列[0]; 写入 dp[3]
    for (let i = 1; i < len; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 长度 就继续
      dp[1] = Math.max(dp[1], dp[0] - prices[i]); // 把 Math.取较大值 DP 表[1], DP 表[0] 减 价格序列[下标 i]); 写入 dp[1]
      dp[2] = Math.max(dp[2], dp[1] + prices[i]); // 把 Math.取较大值 DP 表[2], DP 表[1] 加 价格序列[下标 i]); 写入 dp[2]
      dp[3] = Math.max(dp[3], dp[2] - prices[i]); // 把 Math.取较大值 DP 表[3], DP 表[2] 减 价格序列[下标 i]); 写入 dp[3]
      dp[4] = Math.max(dp[4], dp[3] + prices[i]); // 把 Math.取较大值 DP 表[4], DP 表[3] 加 价格序列[下标 i]); 写入 dp[4]
    }
    return dp[4]; // 返回 DP 表[4]
  }

  const cases: { in: number[]; want: number }[] = [
    { in: [1, 2, 3], want: 2 },
    { in: [1, 2, 3, 4, 5], want: 4 },
    { in: [7, 6, 4, 3, 1], want: 0 },
    { in: [3, 3, 5, 0, 0, 3, 1, 4], want: 6 },
    { in: [1], want: 0 },
    { in: [1, 2], want: 1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = maxProfit(c.in); // 把 maxProfit(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL maxProfit(%o)=%d want %d', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
