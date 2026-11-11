// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144851123
/** 来源: LeetCode 322 零钱兑换 */
export function coinChange(coins: number[], amount: number): number {
  // 定义函数/方法 coinChange
  if (amount < 0) return -1; // 若 目标金额 小于 0，直接返回 减 1
  const dp = new Array(amount + 1).fill(amount + 1); // 把 new Array(目标金额 加 1).fill(目标金额 加 1) 存入 DP 表
  dp[0] = 0; // 把 0; 写入 dp[0]
  for (let a = 1; a <= amount; a++) {
    // 让 数组 从 1 开始计数，数组 不超过 目标金额 就继续
    for (const c of coins) {
      // for (const 字符 of 硬币面额) {
      if (c <= a && dp[a - c] + 1 < dp[a]) dp[a] = dp[a - c] + 1;
    }
  }
  return dp[amount] > amount ? -1 : dp[amount]; // 返回 DP 表[目标金额] 超过 目标金额 ? 减 1 : DP 表[目标金额]
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number, number][] = [
    [[1, 2, 5], 11, 3],
    [[2], 3, -1],
    [[1], 0, 0],
  ];
  for (const [coins, amount, want] of cases) {
    // for (const [硬币面额, 目标金额, want] of cases) {
    const got = coinChange(coins, amount); // 把 coinChange(硬币面额, 目标金额) 存入 got
    if (got !== want)
      throw new Error(
        `FAIL coins=${JSON.stringify(coins)} amount=${amount} want=${want} got=${got}`,
      );
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
