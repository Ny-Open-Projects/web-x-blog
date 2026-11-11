/**
 * LeetCode 877. 石子游戏
 * 方案：3 ) 方案3：数学
 * 来源：https://blog.csdn.net/tyro_java/article/details/145355902
 * 忠实翻译 python/dp/lc_877_石子游戏/solution_3_3_____3___.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function stoneGame(piles: number[]): boolean {
    // 定义函数/方法 stoneGame
    return true; // 返回 true
  }

  const cases: { in: number[]; want: boolean }[] = [
    { in: [5, 3, 4, 5], want: true },
    { in: [], want: true },
    { in: [0, 0], want: true },
    { in: [3, 7, 2, 3], want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = stoneGame(c.in); // 把 stoneGame(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL stoneGame(%o)=%s want %s', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
