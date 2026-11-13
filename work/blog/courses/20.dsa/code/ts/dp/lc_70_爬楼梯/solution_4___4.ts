/**
 ** LeetCode 70. 爬楼梯
 ** 方案：方案4
 ** 来源：https://blog.csdn.net/tyro_java/article/details/130660487
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function climbStairs(n: number): number {
    // 定义函数/方法 climbStairs
    if (n <= 1) return 1; // 若 元素个数 不超过 1，直接返回 1
    let prev = 1,
      cur = 1; // 把 1, 当前值 赋值为 1 存入 前一个
    for (let k = 2; k <= n; k++) {
      // 让 下标 k 从 2 开始计数，下标 k 不超过 元素个数 就继续
      const tmp = cur; // 把 当前值 存入 临时变量
      cur = prev + cur; // 把 前一个 加 当前值 存入 当前值
      prev = tmp; // 把 临时变量 存入 前一个
    }
    return cur; // 返回 当前值
  }
  const cases: Array<{ n: number; want: number }> = [
    { n: 2, want: 2 },
    { n: 3, want: 3 },
    { n: 10, want: 89 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = climbStairs(c.n); // 把 climbStairs(字符.元素个数) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      console.log(`FAIL climbStairs(${c.n})=${got} want ${c.want}`);
      fail = true; // 把 true 存入 fail
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
