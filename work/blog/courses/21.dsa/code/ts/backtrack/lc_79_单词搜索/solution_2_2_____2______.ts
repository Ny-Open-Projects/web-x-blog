// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240191
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function exist(board: string[][] | null, word: string): boolean {
    // 定义函数/方法 exist
    if (!board || board.length === 0 || board[0].length === 0) return false; // 若 取反 棋盘 或 棋盘.长度 全等于 0 或 棋盘[0].长度 全等于 0，直接返回 false
    const rows: number = board.length; // 把 棋盘.长度; 写入 const rows: number
    const cols: number = board[0].length; // 把 棋盘[0].长度; 写入 const cols: number
    function backtrack(r: number, c: number, idx: number): boolean {
      // 定义函数/方法 backtrack
      if (idx === word.length) return true; // 若 idx 全等于 单词.长度，直接返回 true
      if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] !== word[idx])
        return false;
      const temp: string = board[r][c]; // 把 棋盘[右指针][字符]; 写入 const temp: string
      board[r][c] = '#'; // 把 「#」; 写入 board[r][c]
      const found: boolean = // 把  写入 const found: boolean
        backtrack(r + 1, c, idx + 1) ||
        backtrack(r - 1, c, idx + 1) ||
        backtrack(r, c + 1, idx + 1) ||
        backtrack(r, c - 1, idx + 1); // backtrack(右指针, 字符 减 1, idx 加 1);
      board[r][c] = temp; // 把 临时变量; 写入 board[r][c]
      return found; // 返回 found
    }
    for (let r = 0; r < rows; r++) {
      // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
      for (let c = 0; c < cols; c++) {
        // 让 字符 从 0 开始计数，字符 小于 列数 就继续
        if (backtrack(r, c, 0)) return true; // 若 backtrack(右指针, 字符, 0)，直接返回 true
      }
    }
    return false; // 返回 false
  }
  const cases: Array<[string[][] | null, string, boolean]> = [
    [null, 'abc', false],
    [
      [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
      ],
      'ABCCED',
      true,
    ],
    [
      [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
      ],
      'SEE',
      true,
    ],
  ];
  let fail = false; // 把 false 存入 fail
  for (const cs of cases) {
    // for (const cs of cases) {
    const b = cs[0]; // 把 cs[0] 存入 b
    const w = cs[1]; // 把 cs[1] 存入 权重
    const exp = cs[2]; // 把 cs[2] 存入 exp
    const got = exist(b, w); // 把 exist(b, 权重) 存入 got
    if (got !== exp) {
      // 若 got 不等于 exp
      fail = true; // 把 true 存入 fail
      console.log('FAIL exist got ' + got + ' want ' + exp); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
