// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function compareVersion(v1: string, v2: string): number {
    // 定义函数/方法 compareVersion
    const a = v1.split('.'),
      b = v2.split('.'); // 把 v1.split(「.」), b 赋值为 v2.split(「.」) 存入 数组
    const n = Math.max(a.length, b.length); // 把 Math.取较大值 数组.长度, b.长度) 存入 元素个数
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      const x = i < a.length ? parseInt(a[i], 10) : 0; // 把 下标 i 小于 数组.长度 ? 转整数(数组[下标 i]) : 0 存入 x
      const y = i < b.length ? parseInt(b[i], 10) : 0; // 把 下标 i 小于 b.长度 ? 转整数(b[下标 i]) : 0 存入 y
      if (x > y) return 1; // 若 x 超过 y，直接返回 1
      if (x < y) return -1; // 若 x 小于 y，直接返回 减 1
    }
    return 0; // 返回 0
  }
  const cases = [
    { a: '1.01', b: '1.001', want: 0 },
    { a: '1.0', b: '1.0.0', want: 0 },
    { a: '0.1', b: '1.1', want: -1 },
    { a: '1.0.1', b: '1', want: 1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = compareVersion(c.a, c.b); // 把 compareVersion(字符.数组, 字符.b) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
