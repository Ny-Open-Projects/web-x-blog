// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 朴素矩阵乘法：时间复杂度 O(n^3)
  function matrixMultiply(a: number[][], b: number[][]): number[][] {
    // 定义函数/方法 matrixMultiply
    const n = a.length; // 把 数组.长度 存入 元素个数
    const c: number[][] = []; // 把 []; 写入 const c: number[][]
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      c.push(new Array<number>(n).fill(0)); // 把 new Array 小于 number 超过 (元素个数 压入栈/数组尾部
    }
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (let j = 0; j < n; j++) {
        // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
        for (let k = 0; k < n; k++) {
          // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
          c[i][j] += a[i][k] * b[k][j]; // c[i][j]累加 数组[下标 i][下标 k] 乘 b[下标 k][下标 j]
        }
      }
    }
    return c; // 返回 字符
  }

  function eqMat(a: number[][], b: number[][]): boolean {
    // 定义函数/方法 eqMat
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i].length !== b[i].length) return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
      for (let j = 0; j < a[i].length; j++)
        if (a[i][j] !== b[i][j]) return false; // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
    }
    return true; // 返回 true
  }

  const cases: { a: number[][]; b: number[][]; want: number[][] }[] = [
    {
      a: [
        [1, 2],
        [3, 4],
      ],
      b: [
        [5, 6],
        [7, 8],
      ],
      want: [
        [19, 22],
        [43, 50],
      ],
    },
    { a: [[2]], b: [[3]], want: [[6]] },
    {
      a: [
        [1, 0],
        [0, 1],
      ],
      b: [
        [5, 6],
        [7, 8],
      ],
      want: [
        [5, 6],
        [7, 8],
      ],
    },
    {
      a: [
        [0, 0],
        [0, 0],
      ],
      b: [
        [1, 2],
        [3, 4],
      ],
      want: [
        [0, 0],
        [0, 0],
      ],
    },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = matrixMultiply(c.a, c.b); // 把 matrixMultiply(字符.数组, 字符.b) 存入 got
    if (!eqMat(got, c.want)) {
      // 若 取反 eqMat(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL matrixMultiply(%o,%o)=%o want %o',
        c.a,
        c.b,
        got,
        c.want,
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
