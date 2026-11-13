// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function fib(n: number): number {
    // 定义函数/方法 fib
    if (n < 2) return n; // 若 元素个数 小于 2，直接返回 元素个数
    let a = 0,
      b = 1; // 把 0, b 赋值为 1 存入 数组
    for (let i = 2; i <= n; i++) {
      const t = b;
      b = a + b;
      a = t;
    } // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
    return b; // 返回 b
  }
  const cases = [
    { in: 0, want: 0 },
    { in: 1, want: 1 },
    { in: 2, want: 1 },
    { in: 10, want: 55 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = fib(c.in); // 把 fib(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL fib(' + c.in + ')=' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
