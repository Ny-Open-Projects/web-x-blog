/**
 ** LeetCode 69. x 的平方根
 ** 方案：2 ) 方案2：二分查找（记录符合条件的最大 mid）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145233215
 */

function mySqrt(x: number): number {
  // 定义函数/方法 mySqrt
  const X = BigInt(x); // 把 BigInt(x) 存入 X
  let lo = 0n,
    hi = X,
    ans = 0n; // 把 0n, 右边界 赋值为 X, 答案 赋值为 0n 存入 左边界
  while (lo <= hi) {
    // 循环，直到不满足「左边界 不超过 右边界」
    const m = (lo + hi) / 2n; // 把 (左边界 加 右边界) 除以 2n 存入 映射表
    if (m * m <= X) {
      // 若 映射表 乘 映射表 不超过 X
      ans = m; // 把 映射表 存入 答案
      lo = m + 1n; // 把 映射表 加 1n 存入 左边界
    } else {
      // 否则
      hi = m - 1n; // 把 映射表 减 1n 存入 右边界
    }
  }
  return Number(ans); // 返回 Number(答案)
}

// 自检用例：(x, 期望)
const cases: [number, number][] = [
  [4, 2],
  [8, 2],
  [16, 4],
  [2147395599, 46339],
];

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  for (const [x, want] of cases) {
    // for (const [x, want] of cases) {
    const got = mySqrt(x); // 把 mySqrt(x) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(`FAIL: mySqrt(${x})=${got} want ${want}`);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
