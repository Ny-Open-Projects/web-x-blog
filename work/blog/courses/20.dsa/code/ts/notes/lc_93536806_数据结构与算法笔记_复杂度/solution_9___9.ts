// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 递归斐波那契：时间复杂度 O(2^n)，指数级
  function fibRecursive(n: number): number {
    // 定义函数/方法 fibRecursive
    if (n < 2) return n; // 若 元素个数 小于 2，直接返回 元素个数
    return fibRecursive(n - 1) + fibRecursive(n - 2); // 返回 fibRecursive(元素个数 减 1) 加 fibRecursive(元素个数 减 2)
  }

  // 迭代/动态规划斐波那契：时间复杂度 O(n)
  function fibIterative(n: number): number {
    // 定义函数/方法 fibIterative
    if (n < 2) return n; // 若 元素个数 小于 2，直接返回 元素个数
    let a = 0,
      b = 1; // 把 0, b 赋值为 1 存入 数组
    for (let i = 2; i <= n; i++) {
      // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
      const t = a + b; // 把 数组 加 b 存入 另一字符串
      a = b; // 把 b 存入 数组
      b = t; // 把 另一字符串 存入 b
    }
    return b; // 返回 b
  }

  const cases: { n: number; want: number }[] = [
    { n: 0, want: 0 },
    { n: 1, want: 1 },
    { n: 2, want: 1 },
    { n: 10, want: 55 },
    { n: 15, want: 610 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const g1 = fibRecursive(c.n); // 把 fibRecursive(字符.元素个数) 存入 g1
    const g2 = fibIterative(c.n); // 把 fibIterative(字符.元素个数) 存入 g2
    if (g1 !== c.want || g2 !== c.want) {
      // 若 g1 不等于 字符.want 或 g2 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL fib(%d): recursive=%d iterative=%d want %d',
        c.n,
        g1,
        g2,
        c.want,
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
