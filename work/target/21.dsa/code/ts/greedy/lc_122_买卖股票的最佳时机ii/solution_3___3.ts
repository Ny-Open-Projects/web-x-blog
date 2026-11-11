// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134633617
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maxProfit(prices: number[]): number {
    // 定义函数/方法 maxProfit
    let profit = 0; // 把 0 存入 profit
    for (let i = 1; i < prices.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
      if (prices[i] > prices[i - 1]) {
        // 若 价格序列[下标 i] 超过 价格序列[下标 i 减 1]
        profit += prices[i] - prices[i - 1]; // profit累加 价格序列[下标 i] 减 价格序列[下标 i 减 1]
      }
    }
    return profit; // 返回 profit
  }
  const cases: [number[], number][] = [
    [[1, 2, 3], 2],
    [[7, 1, 5, 3, 6, 4], 7],
    [[7, 6, 4, 3, 1], 0],
    [[1], 0],
  ];
  let fail = false; // 把 false 存入 fail
  for (const [prices, want] of cases) {
    // for (const [价格序列, want] of cases) {
    const got = maxProfit(prices); // 把 maxProfit(价格序列) 存入 got
    if (got !== want) {
      fail = true;
      console.log(
        'FAIL maxProfit(' + prices + ') got ' + got + ' want ' + want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
