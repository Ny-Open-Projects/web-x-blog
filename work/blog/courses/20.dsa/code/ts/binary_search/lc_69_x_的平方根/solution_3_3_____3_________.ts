/**
 ** LeetCode 69. x 的平方根
 ** 方案：3 ) 方案3：牛顿迭代法
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145233215
 */

function mySqrt(x: number): number {
  // 定义函数/方法 mySqrt
  const X = BigInt(x); // 把 BigInt(x) 存入 X
  if (X < 2n) return Number(X); // 若 X 小于 2n，直接返回 Number(X)
  let r = X; // 把 X 存入 右指针
  while (r * r > X) {
    // 循环，直到不满足「右指针 乘 右指针 超过 X」
    r = (r + X / r) / 2n; // 把 (右指针 加 X 除以 右指针) 除以 2n 存入 右指针
  }
  return Number(r); // 返回 Number(右指针)
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
