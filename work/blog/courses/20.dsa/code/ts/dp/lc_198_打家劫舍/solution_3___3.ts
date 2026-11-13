/**
 ** LeetCode 198. 打家劫舍
 ** 方案：方案3
 ** 来源：https://blog.csdn.net/tyro_java/article/details/130670245
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function rob(nums: number[]): number {
    // 定义函数/方法 rob
    let prev = 0,
      cur = 0; // 把 0, 当前值 赋值为 0 存入 前一个
    for (const x of nums) {
      // for (const x of 数组) {
      const nxt = Math.max(cur, prev + x); // 把 Math.取较大值 当前值, 前一个 加 x) 存入 nxt
      prev = cur; // 把 当前值 存入 前一个
      cur = nxt; // 把 nxt 存入 当前值
    }
    return cur; // 返回 当前值
  }
  const cases: Array<{ nums: number[]; want: number }> = [
    { nums: [1, 2, 3, 1], want: 4 },
    { nums: [2, 7, 9, 3, 1], want: 12 },
    { nums: [2, 1, 1, 2], want: 4 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = rob(c.nums); // 把 rob(字符.数组) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      console.log(`FAIL rob(${JSON.stringify(c.nums)})=${got} want ${c.want}`);
      fail = true; // 把 true 存入 fail
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
