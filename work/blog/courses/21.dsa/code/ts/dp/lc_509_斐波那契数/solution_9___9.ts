// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function fib(n: number): number {
    // 定义函数/方法 fib
    if (n <= 1) return n; // 若 元素个数 不超过 1，直接返回 元素个数
    let a = 0,
      b = 1; // 把 0, b 赋值为 1 存入 数组
    for (let i = 2; i <= n; i++) {
      // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
      const c = a + b; // 把 数组 加 b 存入 字符
      a = b; // 把 b 存入 数组
      b = c; // 把 字符 存入 b
    }
    return b; // 返回 b
  }
  const cases: [number, number][] = [
    [10, 55],
    [5, 5],
    [0, 0],
    [1, 1],
    [2, 1],
    [20, 6765],
  ];
  let fail = false; // 把 false 存入 fail
  for (const [n, want] of cases) {
    // for (const [元素个数, want] of cases) {
    const got = fib(n); // 把 fib(元素个数) 存入 got
    if (got !== want) {
      fail = true;
      console.log('FAIL fib(' + n + ') got ' + got + ' want ' + want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
