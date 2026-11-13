// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238257
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  type Board = string[][]; // 定义类型
  function solveSudoku(board: Board): void {
    // 定义函数/方法 solveSudoku
    function is_valid(row: number, col: number, num: string): boolean {
      // 定义判定函数 is_valid
      for (let i = 0; i < 9; i++) {
        if (board[i][col] === num) return false;
        if (board[row][i] === num) return false;
      } // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
      const sr = 3 * Math.floor(row / 3),
        sc = 3 * Math.floor(col / 3); // 把 3 乘 向下取整(row 除以 3), sc 赋值为 3 乘 向下取整(col 除以 3) 存入 sr
      for (let i = 0; i < 3; i++)
        for (let j = 0; j < 3; j++)
          if (board[sr + i][sc + j] === num) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
      return true; // 返回 true
    }
    function backtrack(): boolean {
      // 定义函数/方法 backtrack
      for (let row = 0; row < 9; row++)
        for (let col = 0; col < 9; col++) {
          // 让 row 从 0 开始计数，row 小于 9 就继续
          if (board[row][col] === '.') {
            // 若 棋盘[row][col] 全等于 '.'
            for (const num of '123456789') {
              // for(const num of '123456789'){
              if (is_valid(row, col, num)) {
                // 若 is_valid(row,col,num
                board[row][col] = num; // 把 num; 写入 board[row][col]
                if (backtrack()) return true; // 若 backtrack()，直接返回 true
                board[row][col] = '.'; // 把 '.'; 写入 board[row][col]
              }
            }
            return false; // 返回 false
          }
        }
      return true; // 返回 true
    }
    backtrack(); // backtrack();
  }
  const board: Board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
  ];
  solveSudoku(board); // solveSudoku(棋盘);
  const want: Board = [
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
  ];
  let fail = false; // 把 false 存入 fail
  for (let r = 0; r < 9; r++)
    for (let c = 0; c < 9; c++)
      if (board[r][c] !== want[r][c]) {
        fail = true;
        console.log('FAIL', r, c);
      } // 让 右指针 从 0 开始计数，右指针 小于 9 就继续
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
