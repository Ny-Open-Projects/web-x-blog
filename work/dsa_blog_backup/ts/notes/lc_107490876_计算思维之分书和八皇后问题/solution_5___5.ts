/**
 ** LeetCode 107490876. 计算思维之分书和八皇后问题
 ** 八皇后问题（优化回溯，S/L/R 布尔数组标记），行号 0..n-1
 ** 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function nQueensBool(n: number): number[][] {
    // 定义函数/方法 nQueensBool
    const SIZE = n; // 把 元素个数 存入 SIZE
    const colRow: number[] = new Array(SIZE).fill(0); // 把 new Array(SIZE).fill(0); 写入 const colRow: number[]
    const rows: boolean[] = new Array(SIZE).fill(true); // 把 new Array(SIZE).fill(true); 写入 const rows: boolean[]
    const diag1: boolean[] = new Array(2 * SIZE - 1).fill(true); // (col - row + OFFSET)
    const diag2: boolean[] = new Array(2 * SIZE - 1).fill(true); // (col + row)
    const OFFSET = SIZE - 1; // 把 SIZE 减 1 存入 OFFSET
    const results: number[][] = []; // 把 []; 写入 const results: number[][]

    function place(col: number): void {
      // 定义函数/方法 place
      if (col === SIZE) {
        // 若 col 全等于 SIZE
        results.push(colRow.slice()); // 把 colRow 截取 压入栈/数组尾部
        return; // return;
      }
      for (let row = 0; row < SIZE; row++) {
        // 让 row 从 0 开始计数，row 小于 SIZE 就继续
        const d1 = col - row + OFFSET; // 把 col 减 row 加 OFFSET 存入 d1
        const d2 = col + row; // 把 col 加 row 存入 d2
        if (rows[row] && diag1[d1] && diag2[d2]) {
          // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
          colRow[col] = row; // 把 row; 写入 colRow[col]
          rows[row] = false; // 把 false; 写入 rows[row]
          diag1[d1] = false; // 把 false; 写入 diag1[d1]
          diag2[d2] = false; // 把 false; 写入 diag2[d2]
          place(col + 1); // place(col 加 1);
          rows[row] = true; // 把 true; 写入 rows[row]
          diag1[d1] = true; // 把 true; 写入 diag1[d1]
          diag2[d2] = true; // 把 true; 写入 diag2[d2]
        }
      }
    }

    place(0); // place(0);
    return results; // 返回 results
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { n: number; count: number; first: number[] | null }[] = [
    { n: 8, count: 92, first: [0, 4, 7, 5, 2, 6, 1, 3] },
    { n: 1, count: 1, first: [0] },
    { n: 2, count: 0, first: null },
    { n: 4, count: 2, first: [1, 3, 0, 2] },
  ];

  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const sols = nQueensBool(c.n); // 把 nQueensBool(字符.元素个数) 存入 sols
    if (sols.length !== c.count) {
      // 若 sols.长度 不等于 字符.计数
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL n_queens_bool(' +
          c.n +
          ') count=' +
          sols.length +
          ' want ' +
          c.count,
      ); // 打印输出
    }
    if (c.first !== null) {
      // 若 字符.first 不等于 null
      if (sols.length === 0 || !eqArr(sols[0], c.first)) {
        // 若 sols.长度 全等于 0 或 取反 eqArr(sols[0], 字符.first
        fail = true; // 把 true 存入 fail
        console.log(
          'FAIL n_queens_bool(' +
            c.n +
            ') first=' +
            JSON.stringify(sols[0]) +
            ' want ' +
            JSON.stringify(c.first),
        ); // 打印输出
      }
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
