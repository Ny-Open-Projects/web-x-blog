/**
 ** LeetCode 62. 不同路径
 ** 方案：1 ) 方案1: 排列组合
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144847773
 */

function uniquePaths(m: number, n: number): number {
  // 定义函数/方法 uniquePaths
  // 计算组合数 C(m+n-2, m-1) 或 C(m+n-2, n-1)
  // 忠实于 Python 参考实现 ref_uniquePaths 的等价数学形式
  const k = Math.min(m - 1, n - 1); // 把 Math.取较小值 映射表 减 1, 元素个数 减 1) 存入 下标 k
  let result = 1; // 把 1 存入 结果
  for (let i = 1; i <= k; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 下标 k 就继续
    result *= m + n - 1 - i; // 把 (映射表 加 元素个数 减 1 减 下标 i); 写入 result *
    result = Math.floor(result / i); // 确保每一步都是整数除法
  }
  return result; // 返回 结果
}

// 自检用例：(m, n, 期望)
const cases: [number, number, number][] = [
  [3, 7, 28],
  [3, 2, 3],
  [1, 1, 1],
];

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  for (const [m, n, want] of cases) {
    // for (const [映射表, 元素个数, want] of cases) {
    const got = uniquePaths(m, n); // 把 uniquePaths(映射表, 元素个数) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(`FAIL: uniquePaths(${m},${n})=${got} want ${want}`);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
