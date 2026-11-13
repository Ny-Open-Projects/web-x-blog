/**
 ** LeetCode 417. 太平洋大西洋水流问题
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133982215
 ** 方案：方案2（DFS 反向流动，从海洋边界出发）
 */

function pacificAtlantic(matrix: number[][] | null): number[][] {
  // 定义函数/方法 pacificAtlantic
  if (!matrix || matrix.length === 0 || matrix[0].length === 0) return []; // 若 取反 矩阵 或 矩阵.长度 全等于 0 或 矩阵[0].长度 全等于 0，直接返回 []
  const m = matrix.length; // 把 矩阵.长度 存入 映射表
  const n = matrix[0].length; // 把 矩阵[0].长度 存入 元素个数
  const pacific: boolean[][] = Array.from(
    { length: m },
    () => new Array<boolean>(n).fill(false), // new Array 小于 boolean 超过 (元素个数).fill(false)
  );
  const atlantic: boolean[][] = Array.from(
    { length: m },
    () => new Array<boolean>(n).fill(false), // new Array 小于 boolean 超过 (元素个数).fill(false)
  );

  function dfs(r: number, c: number, flow: boolean[][]): void {
    // 定义函数/方法 dfs
    flow[r][c] = true; // 把 true; 写入 flow[r][c]
    const dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];
    for (const [dr, dc] of dirs) {
      // for (const [dr, dc] of dirs) {
      const nr = r + dr; // 把 右指针 加 dr 存入 nr
      const nc = c + dc; // 把 字符 加 dc 存入 nc
      if (
        nr >= 0 &&
        nr < m &&
        nc >= 0 &&
        nc < n &&
        !flow[nr][nc] &&
        matrix[nr][nc] >= matrix[r][c] // 把 矩阵[右指针][字符] 写入 matrix[nr][nc] >
      ) {
        // ) {
        dfs(nr, nc, flow); // dfs(nr, nc, flow);
      }
    }
  }

  for (let r = 0; r < m; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
    dfs(r, 0, pacific); // dfs(右指针, 0, pacific);
    dfs(r, n - 1, atlantic); // dfs(右指针, 元素个数 减 1, atlantic);
  }
  for (let c = 0; c < n; c++) {
    // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
    dfs(0, c, pacific); // dfs(0, 字符, pacific);
    dfs(m - 1, c, atlantic); // dfs(映射表 减 1, 字符, atlantic);
  }

  const res: number[][] = []; // 把 []; 写入 const res: number[][]
  for (let r = 0; r < m; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
    for (let c = 0; c < n; c++) {
      // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
      if (pacific[r][c] && atlantic[r][c]) res.push([r, c]); // 若 pacific[右指针][字符] 且 atlantic[右指针][字符]) 结果 追加 [右指针, 字符]);
    }
  }
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const got = pacificAtlantic([
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
  ]); // ]);
  const expected = [
    [0, 4],
    [1, 3],
    [1, 4],
    [2, 2],
    [3, 0],
    [3, 1],
    [4, 0],
  ];
  if (got.length !== expected.length) throw new Error('length mismatch'); // 若 got.长度 不等于 expected.长度) throw new Error(「长度 mismatch」);
  for (let i = 0; i < expected.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 expected.长度 就继续
    if (got[i][0] !== expected[i][0] || got[i][1] !== expected[i][1])
      throw new Error('cell mismatch at ' + i); // throw new Error(「cell mismatch at 」 加 下标 i);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
