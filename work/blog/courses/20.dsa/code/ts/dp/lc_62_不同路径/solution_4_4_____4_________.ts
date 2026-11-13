/**
 ** LeetCode 62. 不同路径
 ** 方案：4 ) 方案4: 动态规划优化版
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144847773
 */

function uniquePaths(m: number, n: number): number {
  // 定义函数/方法 uniquePaths
  // 一维动态规划（忠实翻译 Python ref_uniquePaths）
  // dp = [1]*n; for _ in range(1, m): for j in range(1, n): dp[j] += dp[j-1]
  const f = new Array(n).fill(1); // 把 new Array(元素个数).fill(1) 存入 f
  for (let i = 1; i < m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
    for (let j = 1; j < n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
      f[j] += f[j - 1]; // f[j]累加 f[下标 j 减 1]
    }
  }
  return f[n - 1]; // 返回 f[元素个数 减 1]
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
