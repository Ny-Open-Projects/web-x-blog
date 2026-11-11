// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853482

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function maxProfit(prices: number[], fee: number): number {
  // 定义函数/方法 maxProfit
  let cash = 0; // 把 0 存入 cash
  let hold = -prices[0]; // 把 减 价格序列[0] 存入 hold
  for (let i = 1; i < prices.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
    cash = Math.max(cash, hold + prices[i] - fee); // 把 Math.取较大值 cash, hold 加 价格序列[下标 i] 减 fee) 存入 cash
    hold = Math.max(hold, cash - prices[i]); // 把 Math.取较大值 hold, cash 减 价格序列[下标 i]) 存入 hold
  }
  return cash; // 返回 cash
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(maxProfit([1, 3, 2, 8, 4, 9], 2), 8, 'maxProfit'); // 断言校验
  assertEq(maxProfit([1], 1), 0, 'maxProfit single'); // 断言校验
  assertEq(maxProfit([1, 2, 3, 4, 5], 1), 3, 'maxProfit 2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
