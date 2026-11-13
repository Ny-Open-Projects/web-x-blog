/**
 ** LeetCode 62. 不同路径
 ** 方案：3 ) 方案3: 动态规划
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144847773
 */

function uniquePaths(m: number, n: number): number {
  // 定义函数/方法 uniquePaths
  // 二维动态规划
  // 忠实于 Python 参考实现 ref_uniquePaths 的 DP 思想
  const f = new Array(m).fill(0).map(() => new Array(n).fill(0));
  for (let i = 0; i < m; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    f[i][0] = 1; // 把 1; 写入 f[i][0]
  }
  for (let j = 0; j < n; j++) {
    // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
    f[0][j] = 1; // 把 1; 写入 f[0][j]
  }
  for (let i = 1; i < m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
    for (let j = 1; j < n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
      f[i][j] = f[i - 1][j] + f[i][j - 1]; // 把 f[下标 i 减 1][下标 j] 加 f[下标 i][下标 j 减 1]; 写入 f[i][j]
    }
  }
  return f[m - 1][n - 1]; // 返回 f[映射表 减 1][元素个数 减 1]
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
