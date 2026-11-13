/**
 * LeetCode 123. 买卖股票的最佳时机 III
 * 方案：2 ) 方案2:动态规划优化空间
 * 来源：https://blog.csdn.net/tyro_java/article/details/144849793
 * 忠实翻译 python/dp/lc_123_买卖股票的最佳时机_iii/solution_2_2_____2_________.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maxProfit(prices: number[]): number {
    // 定义函数/方法 maxProfit
    if (prices.length === 0) {
      // 若 价格序列.长度 全等于 0
      return 0; // 返回 0
    }
    let buy1 = -prices[0]; // 把 减 价格序列[0] 存入 buy1
    let sell1 = 0; // 把 0 存入 sell1
    let buy2 = -prices[0]; // 把 减 价格序列[0] 存入 buy2
    let sell2 = 0; // 把 0 存入 sell2
    for (let i = 1; i < prices.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
      const p = prices[i]; // 把 价格序列[下标 i] 存入 节点
      buy1 = Math.max(buy1, -p); // 把 Math.取较大值 buy1, 减 节点) 存入 buy1
      sell1 = Math.max(sell1, buy1 + p); // 把 Math.取较大值 sell1, buy1 加 节点) 存入 sell1
      buy2 = Math.max(buy2, sell1 - p); // 把 Math.取较大值 buy2, sell1 减 节点) 存入 buy2
      sell2 = Math.max(sell2, buy2 + p); // 把 Math.取较大值 sell2, buy2 加 节点) 存入 sell2
    }
    return sell2; // 返回 sell2
  }

  const cases: { in: number[]; want: number }[] = [
    { in: [3, 3, 5, 0, 0, 3, 1, 4], want: 6 },
    { in: [1, 2, 3, 4, 5], want: 4 },
    { in: [7, 6, 4, 3, 1], want: 0 },
    { in: [1], want: 0 },
    { in: [], want: 0 },
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
