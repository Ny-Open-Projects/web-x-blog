/**
 ** LeetCode 51. N 皇后
 ** 方案2: 基于集合+棋盘构建的回溯（忠实翻译 python 参考实现）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145239695
 */

function solveNQueens(n: number): string[][] {
  // 定义函数/方法 solveNQueens
  const res: string[][] = []; // 把 []; 写入 const res: string[][]
  const cols = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 列数
  const diag1 = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 diag1
  const diag2 = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 diag2
  function backtrack(r: number, board: string[][]): void {
    // 定义函数/方法 backtrack
    if (r === n) {
      // 若 右指针 全等于 元素个数
      res.push(board.map((row) => row.join('')));
      return; // return;
    }
    for (let c = 0; c < n; c++) {
      // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
      if (cols.has(c) || diag1.has(r - c) || diag2.has(r + c)) continue;
      cols.add(c); // 列数 追加 字符);
      diag1.add(r - c); // diag1 追加 右指针 减 字符);
      diag2.add(r + c); // diag2 追加 右指针 加 字符);
      const rowArr: string[] = new Array(n).fill('.'); // 把 new Array(元素个数).fill('.'); 写入 const rowArr: string[]
      rowArr[c] = 'Q'; // 把 'Q'; 写入 rowArr[c]
      board.push(rowArr); // 把 rowArr 压入栈/数组尾部
      backtrack(r + 1, board); // backtrack(右指针 加 1, 棋盘);
      board.pop(); // 弹出栈顶元素
      cols.delete(c); // 列数.delete(字符);
      diag1.delete(r - c); // diag1.delete(右指针 减 字符);
      diag2.delete(r + c); // diag2.delete(右指针 加 字符);
    }
  }
  backtrack(0, []); // backtrack(0, []);
  return res; // 返回 结果
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
