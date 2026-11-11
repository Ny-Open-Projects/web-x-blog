/**
 * LeetCode 518. 零钱兑换 II
 * 方案：1 ) 方案1: 递归搜索 + 保存计算结果 = 记忆化搜索
 * 来源：https://blog.csdn.net/tyro_java/article/details/144852221
 * 忠实翻译 python/dp/lc_518_零钱兑换_ii/solution_1_1_____1_______________________.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function change(amount: number, coins: number[]): number {
    // 定义函数/方法 change
    const n = coins.length; // 把 硬币面额.长度 存入 元素个数
    const memo: number[][] = Array.from({ length: n }, () =>
      new Array(amount + 1).fill(-1),
    );

    function dfs(i: number, c: number): number {
      // 定义函数/方法 dfs
      if (i < 0) {
        // 若 下标 i 小于 0
        return c === 0 ? 1 : 0; // 返回 字符 全等于 0 ? 1 : 0
      }
      if (memo[i][c] !== -1) {
        // 若 记忆化表[下标 i][字符] 不等于 减 1
        return memo[i][c]; // 返回 记忆化表[下标 i][字符]
      }
      if (c < coins[i]) {
        // 若 字符 小于 硬币面额[下标 i]
        memo[i][c] = dfs(i - 1, c); // 把 dfs(下标 i 减 1, 字符); 写入 memo[i][c]
        return memo[i][c]; // 返回 记忆化表[下标 i][字符]
      }
      memo[i][c] = dfs(i - 1, c) + dfs(i, c - coins[i]);
      return memo[i][c]; // 返回 记忆化表[下标 i][字符]
    }

    return dfs(n - 1, amount); // 返回 dfs(元素个数 减 1, 目标金额)
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
