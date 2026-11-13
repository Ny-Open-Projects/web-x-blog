/**
 ** LeetCode 48. 旋转矩阵
 ** 方案：方案1
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134032039
 */

function rotate(matrix: number[][]): void {
  // 定义函数/方法 rotate
  const n = matrix.length; // 把 矩阵.长度 存入 元素个数
  for (let i = 0; i < Math.floor(n / 2); i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 向下取整(元素个数 除以 2) 就继续
    const tmp = matrix[i]; // 把 矩阵[下标 i] 存入 临时变量
    matrix[i] = matrix[n - 1 - i]; // 把 矩阵[元素个数 减 1 减 下标 i]; 写入 matrix[i]
    matrix[n - 1 - i] = tmp; // 把 临时变量; 写入 matrix[n - 1 - i]
  }
  for (let i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (let j = 0; j < i; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
      const tmp = matrix[i][j]; // 把 矩阵[下标 i][下标 j] 存入 临时变量
      matrix[i][j] = matrix[j][i]; // 把 矩阵[下标 j][下标 i]; 写入 matrix[i][j]
      matrix[j][i] = tmp; // 把 临时变量; 写入 matrix[j][i]
    }
  }
}

function eqMatrix(a: number[][], b: number[][]): boolean {
  // 定义函数/方法 eqMatrix
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i].length !== b[i].length) return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
    for (let j = 0; j < a[i].length; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
      if (a[i][j] !== b[i][j]) return false; // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]，直接返回 false
    }
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[][], number[][]][] = [
    [
      [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
      ],
      [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
      ],
    ],
    [
      [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
      ],
      [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
      ],
    ],
  ];
  for (const [input, expected] of cases) {
    // for (const [input, expected] of cases) {
    rotate(input); // rotate(input);
    if (!eqMatrix(input, expected)) {
      // 若 取反 eqMatrix(input, expected
      throw new Error(
        'FAIL: got ' +
          JSON.stringify(input) +
          ' expected ' +
          JSON.stringify(expected),
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
