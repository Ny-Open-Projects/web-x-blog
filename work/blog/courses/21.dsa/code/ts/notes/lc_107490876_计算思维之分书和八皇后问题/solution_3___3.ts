/**
 ** LeetCode 107490876. 计算思维之分书和八皇后问题
 ** 八皇后问题（逐列放置 + 显式安全检查 isSafe），行号 1..n
 ** 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function nQueensSafe(n: number): number[][] {
    // 定义函数/方法 nQueensSafe
    const results: number[][] = []; // 把 []; 写入 const results: number[][]
    const board: number[] = new Array(n).fill(0); // board[col] = row

    function isSafe(col: number, row: number): boolean {
      // 定义判定函数 isSafe
      for (let c = 0; c < col; c++) {
        // 让 字符 从 0 开始计数，字符 小于 col 就继续
        if (
          board[c] === row ||
          Math.abs(board[c] - row) === Math.abs(c - col)
        ) {
          return false; // 返回 false
        }
      }
      return true; // 返回 true
    }

    function place(col: number): void {
      // 定义函数/方法 place
      if (col === n) {
        // 若 col 全等于 元素个数
        results.push(board.slice()); // 把 棋盘 截取 压入栈/数组尾部
        return; // return;
      }
      for (let row = 1; row <= n; row++) {
        // 让 row 从 1 开始计数，row 不超过 元素个数 就继续
        if (isSafe(col, row)) {
          // 若 isSafe(col, row
          board[col] = row; // 把 row; 写入 board[col]
          place(col + 1); // place(col 加 1);
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
    { n: 8, count: 92, first: [1, 5, 8, 6, 3, 7, 2, 4] },
    { n: 1, count: 1, first: [1] },
    { n: 2, count: 0, first: null },
    { n: 4, count: 2, first: [2, 4, 1, 3] },
  ];

  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const sols = nQueensSafe(c.n); // 把 nQueensSafe(字符.元素个数) 存入 sols
    if (sols.length !== c.count) {
      // 若 sols.长度 不等于 字符.计数
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL n_queens_safe(' +
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
          'FAIL n_queens_safe(' +
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
