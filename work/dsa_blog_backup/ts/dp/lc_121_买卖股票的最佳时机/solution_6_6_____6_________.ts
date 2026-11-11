/**
 ** LeetCode 121. 买卖股票的最佳时机
 ** 方案：6 ) 方案6: 双状态滚动
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144849130
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maxProfit(prices: number[]): number {
    // 定义函数/方法 maxProfit（O(n)：显式 dp0/dp1 滚动）
    let dp0 = 0; // 第 i 天结束、未持股的最大利润
    let dp1 = -prices[0]; // 第 i 天结束、持股的最大利润
    for (let i = 1; i < prices.length; i++) {
      // 逐日状态转移
      dp0 = Math.max(dp0, dp1 + prices[i]); // 维持未持有 或 今天卖出
      dp1 = Math.max(dp1, -prices[i]); // 维持持股 或 今天买入
    }
    return dp0; // 返回 dp0
  }
  const cases: Array<{ prices: number[]; want: number }> = [
    { prices: [7, 1, 5, 3, 6, 4], want: 5 },
    { prices: [7, 6, 4, 3, 1], want: 0 },
    { prices: [1, 2, 3], want: 2 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = maxProfit(c.prices); // 把 maxProfit(字符.价格序列) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      console.log(
        `FAIL maxProfit(${JSON.stringify(c.prices)})=${got} want ${c.want}`,
      );
      fail = true; // 把 true 存入 fail
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
