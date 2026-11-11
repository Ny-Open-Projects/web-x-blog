// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function grayCode(n: number): number[] {
    // 定义函数/方法 grayCode
    const res = new Array(1 << n); // 把 new Array(1 小于 小于 元素个数) 存入 结果
    for (let i = 0; i < 1 << n; i++) res[i] = i ^ (i >> 1); // 让 下标 i 从 0 开始计数，下标 i 小于 (1 小于 小于 元素个数) 就继续
    return res; // 返回 结果
  }
  const cases = [
    { in: 0, want: [0] },
    { in: 1, want: [0, 1] },
    { in: 2, want: [0, 1, 3, 2] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = grayCode(c.in); // 把 grayCode(字符.in) 存入 got
    if (got.length !== c.want.length || got.some((v, i) => v !== c.want[i])) {
      fail = true;
      console.log('FAIL ' + got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
