/**
 ** LeetCode 107490876. 计算思维之分书和八皇后问题
 ** 八皇后问题（简洁递归版）：以 (row, col) 记录已放置皇后，行号 0..n-1
 ** 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function nQueensSimple(n: number): number[][] {
    // 定义函数/方法 nQueensSimple
    const positions: [number, number][] = []; // 已放置的 (row, col)
    const solutions: number[][] = []; // 把 []; 写入 const solutions: number[][]

    function safe(r: number, c: number): boolean {
      // 定义函数/方法 safe
      for (const [rr, cc] of positions) {
        // for (const [rr, cc] of positions) {
        if (rr === r || Math.abs(rr - r) === Math.abs(cc - c)) {
          // 若 rr 全等于 右指针 或 Math.取绝对值 rr 减 右指针) 全等于 Math.取绝对值 cc 减 字符
          return false; // 返回 false
        }
      }
      return true; // 返回 true
    }

    function solve(col: number): void {
      // 定义函数/方法 solve
      if (col === n) {
        // 若 col 全等于 元素个数
        solutions.push(positions.map((p) => p[0]));
        return; // return;
      }
      for (let r = 0; r < n; r++) {
        // 让 右指针 从 0 开始计数，右指针 小于 元素个数 就继续
        if (safe(r, col)) {
          // 若 safe(右指针, col
          positions.push([r, col]); // 把 [右指针, col] 压入栈/数组尾部
          solve(col + 1); // solve(col 加 1);
          positions.pop(); // 弹出栈顶元素
        }
      }
    }

    solve(0); // solve(0);
    return solutions; // 返回 solutions
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
    const sols = nQueensSimple(c.n); // 把 nQueensSimple(字符.元素个数) 存入 sols
    if (sols.length !== c.count) {
      // 若 sols.长度 不等于 字符.计数
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL n_queens_simple(' +
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
          'FAIL n_queens_simple(' +
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
