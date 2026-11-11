/**
 ** LeetCode 121. 买卖股票的最佳时机
 ** 方案：4 ) 方案4: 前缀最低价数组
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144849130
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maxProfit(prices: number[]): number {
    // 定义函数/方法 maxProfit（O(n)：min 数组 + 一次线性组合）
    const n = prices.length; // 元素个数
    if (n === 0) return 0; // 空数组守卫
    const minUpTo = new Array(n).fill(0); // minUpTo[i] = 前 i+1 天的最低价
    minUpTo[0] = prices[0]; // 初始化首元素
    for (let i = 1; i < n; i++)
      minUpTo[i] = Math.min(minUpTo[i - 1], prices[i]); // 前缀最低价
    let maxprofit = 0; // 最大利润
    for (let i = 1; i < n; i++)
      maxprofit = Math.max(maxprofit, prices[i] - minUpTo[i - 1]); // 今天卖、之前最低买
    return maxprofit; // 返回 maxprofit
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
