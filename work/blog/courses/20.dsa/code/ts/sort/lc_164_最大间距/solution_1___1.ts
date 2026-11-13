// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maximumGap(nums: number[]): number {
    // 定义函数/方法 maximumGap
    if (nums.length < 2) return 0; // 若 数组.长度 小于 2，直接返回 0
    const a = nums.slice().sort((x, y) => x - y);
    let max_gap = 0; // 把 0 存入 max_gap
    for (let i = 1; i < a.length; i++)
      max_gap = Math.max(max_gap, a[i] - a[i - 1]); // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
    return max_gap; // 返回 max_gap
  }
  function eq(a: number, b: number): boolean {
    return a === b;
  } // 定义函数/方法 eq
  const cases = [
    { in: [1, 2, 3], want: 1 },
    { in: [3, 6, 9, 1], want: 3 },
    { in: [10], want: 0 },
    { in: [], want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = maximumGap(c.in); // 把 maximumGap(字符.in) 存入 got
    if (!eq(c.want, got)) {
      fail = true;
      console.log(
        'FAIL maximumGap(' +
          JSON.stringify(c.in) +
          ')=' +
          got +
          ' want ' +
          c.want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
