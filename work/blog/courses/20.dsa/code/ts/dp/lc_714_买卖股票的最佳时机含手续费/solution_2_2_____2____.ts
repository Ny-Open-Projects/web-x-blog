// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853482

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function maxProfit(prices: number[], fee: number): number {
  // 定义函数/方法 maxProfit
  let cash = 0;
  let hold = -prices[0]; // 把 0; let hold 赋值为 减 价格序列[0] 存入 cash
  for (let i = 1; i < prices.length; i++) {
    cash = Math.max(cash, hold + prices[i] - fee);
    hold = Math.max(hold, cash - prices[i]);
  } // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
  return cash; // 返回 cash
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(maxProfit([1, 3, 2, 8, 4, 9], 2), 8, 'mp1'); // 断言校验
  assertEq(maxProfit([1], 1), 0, 'mp2'); // 断言校验
  assertEq(maxProfit([1, 2, 3, 4, 5], 1), 3, 'mp3'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
