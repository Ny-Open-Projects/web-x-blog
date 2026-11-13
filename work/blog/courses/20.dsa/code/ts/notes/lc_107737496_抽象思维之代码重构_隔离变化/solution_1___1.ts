// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

class Matrix {
  // 定义类型
  N: number;
  M: number[][]; // N: number; M: number[][];
  constructor(size: number) {
    this.N = size;
    this.M = Array.from({ length: size }, () => new Array(size).fill(0));
  }
  fill(num: number, begin: number, size: number): void {
    // fill(num: number, begin: number, 大小: number): void {
    if (size === 0) return; // 若 大小 全等于 0) return;
    if (size === 1) {
      this.M[begin][begin] = num;
      return;
    } // 若 大小 全等于 1) { this.M[begin][begin] 赋值为 num; return; }
    for (let j = 0; j < size - 1; j++) {
      this.M[begin + j][begin] = num;
      num++;
    } // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
    for (let j = 0; j < size - 1; j++) {
      this.M[begin + size - 1][begin + j] = num;
      num++;
    } // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
    for (let j = size - 1; j > 0; j--) {
      this.M[begin + j][begin + size - 1] = num;
      num++;
    } // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
    for (let j = size - 1; j > 0; j--) {
      this.M[begin][begin + j] = num;
      num++;
    } // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
    this.fill(num, begin + 1, size - 2); // this.fill(num, begin 加 1, 大小 减 2);
  }
}
function fmtRow(row: number[]): string {
  return row.map((x) => x.toString().padStart(2, ' ')).join(' ');
} // 定义函数/方法 fmtRow
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const m = new Matrix(6);
  m.fill(1, 0, 6); // 把 new Matrix(6); 映射表.fill(1, 0, 6) 存入 映射表
  assertEq(
    m.M.map(fmtRow),
    [
      ' 1 20 19 18 17 16',
      ' 2 21 32 31 30 15',
      ' 3 22 33 36 29 14',
      ' 4 23 34 35 28 13',
      ' 5 24 25 26 27 12',
      ' 6  7  8  9 10 11',
    ],
    'spiral6',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
