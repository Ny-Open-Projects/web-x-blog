/**
 ** LeetCode 62. 不同路径
 ** 方案：2 ）方案2: 组合优化版
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144847773
 */

function uniquePaths(m: number, n: number): number {
  // 定义函数/方法 uniquePaths
  // 组合优化版（单循环累加）
  // 忠实于 Python 参考实现 ref_uniquePaths 的等价数学形式
  let ans = 1; // 把 1 存入 答案
  for (let x = n, y = 1; y < m; ++x, ++y) {
    // 让 x 从 元素个数, y 赋值为 1 开始计数，y 小于 映射表 就继续
    ans = Math.floor((ans * x) / y); // 把 向下取整(答案 乘 x 除以 y) 存入 答案
  }
  return ans; // 返回 答案
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
