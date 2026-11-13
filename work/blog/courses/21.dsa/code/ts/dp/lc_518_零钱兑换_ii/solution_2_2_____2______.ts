/**
 * LeetCode 518. 零钱兑换 II
 * 方案：2 ) 方案2: 动态规划
 * 来源：https://blog.csdn.net/tyro_java/article/details/144852221
 * 忠实翻译 python/dp/lc_518_零钱兑换_ii/solution_2_2_____2______.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function change(amount: number, coins: number[]): number {
    // 定义函数/方法 change
    const dp: number[] = new Array(amount + 1).fill(0); // 把 new Array(目标金额 加 1).fill(0); 写入 const dp: number[]
    dp[0] = 1; // 把 1; 写入 dp[0]
    for (const coin of coins) {
      // for (const coin of 硬币面额) {
      for (let c = coin; c <= amount; c++) {
        // 让 字符 从 coin 开始计数，字符 不超过 目标金额 就继续
        dp[c] += dp[c - coin]; // dp[c]累加 DP 表[字符 减 coin]
      }
    }
    return dp[amount]; // 返回 DP 表[目标金额]
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
