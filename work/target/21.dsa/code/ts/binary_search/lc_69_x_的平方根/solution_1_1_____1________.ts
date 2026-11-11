/**
 ** LeetCode 69. x 的平方根
 ** 方案：1 ) 方案1：二分查找（忠实翻译 Python ref_mySqrt）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145233215
 */

function mySqrt(x: number): number {
  // 定义函数/方法 mySqrt
  const X = BigInt(x); // 把 BigInt(x) 存入 X
  if (X < 2n) return Number(X); // 若 X 小于 2n，直接返回 Number(X)
  let lo = 1n,
    hi = X / 2n; // 把 1n, 右边界 赋值为 X 除以 2n 存入 左边界
  while (lo <= hi) {
    // 循环，直到不满足「左边界 不超过 右边界」
    const m = (lo + hi) / 2n; // 把 (左边界 加 右边界) 除以 2n 存入 映射表
    if (m * m <= X && X < (m + 1n) * (m + 1n)) return Number(m);
    else if (m * m > X)
      hi = m - 1n; // 否则，若 映射表 乘 映射表 超过 X) 右边界 赋值为 映射表 减 1n;
    else lo = m + 1n; // 否则
  }
  return Number(lo); // 返回 Number(左边界)
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
