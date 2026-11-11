/**
 ** LeetCode 54. 螺旋矩阵
 ** 方案：方案1
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134026430
 */

export function spiralOrder(matrix: number[][]): number[] {
  // 定义函数/方法 spiralOrder
  if (!matrix || matrix.length === 0 || matrix[0].length === 0) return []; // 若 取反 矩阵 或 矩阵.长度 全等于 0 或 矩阵[0].长度 全等于 0，直接返回 []
  const result: number[] = []; // 把 []; 写入 const result: number[]
  let top = 0; // 把 0 存入 top
  let bottom = matrix.length - 1; // 把 矩阵.长度 减 1 存入 bottom
  let left = 0; // 把 0 存入 左边界
  let right = matrix[0].length - 1; // 把 矩阵[0].长度 减 1 存入 右边界
  while (top <= bottom && left <= right) {
    // 循环，直到不满足「top 不超过 bottom 且 左边界 不超过 右边界」
    for (let i = left; i <= right; i++) result.push(matrix[top][i]); // 让 下标 i 从 左边界 开始计数，下标 i 不超过 右边界 就继续
    top++; // top 加一
    for (let i = top; i <= bottom; i++) result.push(matrix[i][right]); // 让 下标 i 从 top 开始计数，下标 i 不超过 bottom 就继续
    right--; // 右边界 减一
    if (top <= bottom) {
      // 若 top 不超过 bottom
      for (let i = right; i >= left; i--) result.push(matrix[bottom][i]); // 让 下标 i 从 右边界 开始计数，下标 i 不低于 左边界 就继续
      bottom--; // bottom 减一
    }
    if (left <= right) {
      // 若 左边界 不超过 右边界
      for (let i = bottom; i >= top; i--) result.push(matrix[i][left]); // 让 下标 i 从 bottom 开始计数，下标 i 不低于 top 就继续
      left++; // 左边界 加一
    }
  }
  return result; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (JSON.stringify(spiralOrder([])) !== '[]') throw new Error('FAILED empty');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
