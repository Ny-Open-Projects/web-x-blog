/**
 ** LeetCode 121. 买卖股票的最佳时机
 ** 方案：5 ) 方案5: 分治
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144849130
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maxProfit(prices: number[]): number {
    // 定义函数/方法 maxProfit（分治：左半最优、右半最优、跨中点差）
    if (prices.length < 2) return 0; // 少于两天无交易
    const solve = (lo: number, hi: number): [number, number, number] => {
      // 返回 [区间和? 不需要, 区间min, 区间最优利润]
      if (hi - lo === 1) return [prices[lo], 0]; // 单元素：[min, best]
      const mid = (lo + hi) >> 1;
      const [lMin, lBest] = solve(lo, mid);
      const [rMin, rBest] = solve(mid, hi);
      const cross = rMaxOf(prices, mid, hi) - lMin; // 跨中点：右半最大卖出 - 左半最低买入
      return [
        Math.min(lMin, rMin),
        Math.max(Math.max(lBest, rBest), cross < 0 ? 0 : cross),
      ];
    };
    function rMaxOf(arr: number[], lo: number, hi: number): number {
      // [lo,hi) 区间最大值
      let mx = -Infinity;
      for (let i = lo; i < hi; i++) if (arr[i] > mx) mx = arr[i];
      return mx;
    }
    return solve(0, prices.length)[1]; // 返回区间最优利润
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
