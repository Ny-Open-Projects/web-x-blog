/**
 ** LeetCode 51. N 皇后
 ** 方案1: 基于集合的回溯（忠实翻译 python 参考实现）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145239695
 */

function solveNQueens(n: number): string[][] {
  // 定义函数/方法 solveNQueens
  const solutions: string[][] = []; // 把 []; 写入 const solutions: string[][]
  const queens: number[] = new Array(n).fill(-1); // 把 new Array(元素个数).fill( 减 1); 写入 const queens: number[]
  const columns = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 columns
  const diagonal1 = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 diagonal1
  const diagonal2 = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 diagonal2
  function generateBoard(): string[] {
    // 定义函数/方法 generateBoard
    const board: string[] = []; // 把 []; 写入 const board: string[]
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      const rowArr = new Array(n).fill('.'); // 把 new Array(元素个数).fill('.') 存入 rowArr
      rowArr[queens[i]] = 'Q'; // 把 'Q'; 写入 rowArr[queens[i]]
      board.push(rowArr.join('')); // 把 rowArr.join('' 压入栈/数组尾部
    }
    return board; // 返回 棋盘
  }
  function backtrack(row: number): void {
    // 定义函数/方法 backtrack
    if (row === n) {
      // 若 row 全等于 元素个数
      solutions.push(generateBoard()); // 把 generateBoard( 压入栈/数组尾部
      return; // return;
    }
    for (let col = 0; col < n; col++) {
      // 让 col 从 0 开始计数，col 小于 元素个数 就继续
      if (
        columns.has(col) ||
        diagonal1.has(row - col) ||
        diagonal2.has(row + col)
      )
        continue;
      queens[row] = col; // 把 col; 写入 queens[row]
      columns.add(col); // columns 追加 col);
      diagonal1.add(row - col); // diagonal1 追加 row 减 col);
      diagonal2.add(row + col); // diagonal2 追加 row 加 col);
      backtrack(row + 1); // backtrack(row 加 1);
      columns.delete(col); // columns.delete(col);
      diagonal1.delete(row - col); // diagonal1.delete(row 减 col);
      diagonal2.delete(row + col); // diagonal2.delete(row 加 col);
    }
  }
  backtrack(0); // backtrack(0);
  return solutions; // 返回 solutions
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function norm(x: string[][]): string {
    // 定义函数/方法 norm
    return x
      .map((b) => b.join('/'))
      .sort()
      .join('|');
  }
  let fail = false; // 把 false 存入 fail
  if (norm(solveNQueens(1)) !== norm([['Q']])) {
    fail = true;
    console.log('FAIL n=1');
  }
  const want4 = [
    ['.Q..', '...Q', 'Q...', '..Q.'],
    ['..Q.', 'Q...', '...Q', '.Q..'],
  ];
  if (norm(solveNQueens(4)) !== norm(want4)) {
    fail = true;
    console.log('FAIL n=4 got=' + JSON.stringify(solveNQueens(4)));
  }
  if (solveNQueens(5).length !== 10) {
    fail = true;
    console.log('FAIL n=5 count');
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
