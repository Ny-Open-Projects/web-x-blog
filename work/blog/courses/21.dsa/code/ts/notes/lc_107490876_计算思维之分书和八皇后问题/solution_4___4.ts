/**
 ** LeetCode 107490876. 计算思维之分书和八皇后问题
 ** 八皇后问题（栈/迭代回溯）：用显式栈代替递归，行号 1..n
 ** 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function nQueensStack(n: number): number[][] {
    // 定义函数/方法 nQueensStack
    function valid(x: number, a: number[]): boolean {
      // 定义函数/方法 valid
      const y = a.length + 1; // 把 数组.长度 加 1 存入 y
      for (let i = 1; i < y; i++) {
        // 让 下标 i 从 1 开始计数，下标 i 小于 y 就继续
        if (x === a[i - 1] || Math.abs(y - i) === Math.abs(x - a[i - 1])) {
          return false; // 返回 false
        }
      }
      return true; // 返回 true
    }

    const solutions: number[][] = []; // 把 []; 写入 const solutions: number[][]
    const stack: number[][] = [[]]; // 把 [[]]; 写入 const stack: number[][]
    while (stack.length > 0) {
      // 循环，直到不满足「栈.长度 超过 0」
      const a = stack.pop()!; // 把 栈 弹出 )取反 存入 数组
      if (a.length === n) {
        // 若 数组.长度 全等于 元素个数
        solutions.push(a); // 把 数组 压入栈/数组尾部
      } else {
        // 否则
        for (let i = 1; i <= n; i++) {
          // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
          if (valid(i, a)) {
            // 若 valid(下标 i, 数组
            stack.push(a.concat([i])); // 注意：是追加新元素，不是拼接 a[i]
          }
        }
      }
    }
    return solutions; // 返回 solutions
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { n: number; count: number; first: number[] | null }[] = [
    { n: 8, count: 92, first: [8, 4, 1, 3, 6, 2, 7, 5] },
    { n: 1, count: 1, first: [1] },
    { n: 2, count: 0, first: null },
    { n: 4, count: 2, first: [3, 1, 4, 2] },
  ];

  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const sols = nQueensStack(c.n); // 把 nQueensStack(字符.元素个数) 存入 sols
    if (sols.length !== c.count) {
      // 若 sols.长度 不等于 字符.计数
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL n_queens_stack(' +
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
          'FAIL n_queens_stack(' +
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
