/**
 * LeetCode 518. 零钱兑换 II
 * 方案：3 ) 方案3: 动态规划优化版
 * 来源：https://blog.csdn.net/tyro_java/article/details/144852221
 * 忠实翻译 python/dp/lc_518_零钱兑换_ii/solution_3_3_____3_________.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function change(amount: number, coins: number[]): number {
    // 定义函数/方法 change
    const n = coins.length; // 把 硬币面额.长度 存入 元素个数
    const f: number[][] = Array.from({ length: n + 1 }, () =>
      new Array(amount + 1).fill(0),
    );
    f[0][0] = 1; // 把 1; 写入 f[0][0]
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (let c = 0; c <= amount; c++) {
        // 让 字符 从 0 开始计数，字符 不超过 目标金额 就继续
        if (c < coins[i]) {
          // 若 字符 小于 硬币面额[下标 i]
          f[i + 1][c] = f[i][c]; // 把 f[下标 i][字符]; 写入 f[i + 1][c]
        } else {
          // 否则
          f[i + 1][c] = f[i][c] + f[i + 1][c - coins[i]]; // 把 f[下标 i][字符] 加 f[下标 i 加 1][字符 减 硬币面额[下标 i]]; 写入 f[i + 1][c]
        }
      }
    }
    return f[n][amount]; // 返回 f[元素个数][目标金额]
  }

  const cases: { amount: number; coins: number[]; want: number }[] = [
    { amount: 5, coins: [1, 2, 5], want: 4 },
    { amount: 3, coins: [2], want: 0 },
    { amount: 10, coins: [1, 2, 5], want: 10 },
    { amount: 0, coins: [1, 2], want: 1 },
    { amount: 5, coins: [], want: 0 },
    { amount: 4, coins: [1, 1, 2, 2], want: 14 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = change(c.amount, c.coins); // 把 change(字符.目标金额, 字符.硬币面额) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL change(%d, %o)=%d want %d',
        c.amount,
        c.coins,
        got,
        c.want,
      ); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
