// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maximumGap(nums: number[]): number {
    // 定义函数/方法 maximumGap
    if (nums.length < 2) return 0; // 若 数组.长度 小于 2，直接返回 0
    const max_val = Math.max(...nums); // 把 Math.取较大值 ...数组) 存入 max_val
    let radix = 1; // 把 1 存入 radix
    const a = nums.slice(); // 把 数组 截取 ) 存入 数组
    while (max_val >= radix) {
      // 循环，直到不满足「max_val 不低于 radix」
      const bucket = new Array(10).fill(0); // 把 new Array(10).fill(0) 存入 bucket
      for (const num of a) bucket[Math.floor(num / radix) % 10]++;
      for (let i = 1; i < 10; i++) bucket[i] += bucket[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 10 就继续
      const tmp = new Array(a.length).fill(0); // 把 new Array(数组.长度).fill(0) 存入 临时变量
      for (let i = a.length - 1; i >= 0; i--) {
        // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 不低于 0 就继续
        const idx = Math.floor(a[i] / radix) % 10; // 把 向下取整(数组[下标 i] 除以 radix) 对…取模 10 存入 idx
        tmp[bucket[idx] - 1] = a[i]; // 把 数组[下标 i]; 写入 tmp[bucket[idx] - 1]
        bucket[idx]--; // bucket[idx] 减一 ;
      }
      for (let i = 0; i < a.length; i++) a[i] = tmp[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      radix *= 10; // 把 10; 写入 radix *
    }
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
