/**
 ** LeetCode 51. N 皇后
 ** 方案3: 布尔数组回溯（忠实翻译 python 参考实现）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145239695
 */

function solveNQueens(n: number): string[][] {
  // 定义函数/方法 solveNQueens
  const res: string[][] = []; // 把 []; 写入 const res: string[][]
  const cols: boolean[] = new Array(n).fill(false); // 把 new Array(元素个数).fill(false); 写入 const cols: boolean[]
  const diag1: boolean[] = new Array(2 * n).fill(false); // 把 new Array(2 乘 元素个数).fill(false); 写入 const diag1: boolean[]
  const diag2: boolean[] = new Array(2 * n).fill(false); // 把 new Array(2 乘 元素个数).fill(false); 写入 const diag2: boolean[]
  const board: string[][] = []; // 把 []; 写入 const board: string[][]
  function backtrack(r: number): void {
    // 定义函数/方法 backtrack
    if (r === n) {
      // 若 右指针 全等于 元素个数
      res.push(board.map((row) => row.join('')));
      return; // return;
    }
    for (let c = 0; c < n; c++) {
      // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
      if (cols[c] || diag1[r - c + n] || diag2[r + c]) continue;
      cols[c] = diag1[r - c + n] = diag2[r + c] = true;
      const rowArr: string[] = new Array(n).fill('.'); // 把 new Array(元素个数).fill('.'); 写入 const rowArr: string[]
      rowArr[c] = 'Q'; // 把 'Q'; 写入 rowArr[c]
      board.push(rowArr); // 把 rowArr 压入栈/数组尾部
      backtrack(r + 1); // backtrack(右指针 加 1);
      board.pop(); // 弹出栈顶元素
      cols[c] = diag1[r - c + n] = diag2[r + c] = false;
    }
  }
  backtrack(0); // backtrack(0);
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
