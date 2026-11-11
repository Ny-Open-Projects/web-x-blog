// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 汉诺塔：递归解法，时间复杂度 O(2^n)
  function hanoi(
    n: number,
    src: string,
    aux: string,
    dst: string,
    moves: string[] = [],
  ): string[] {
    // 定义函数/方法 hanoi
    if (n === 1) {
      // 若 元素个数 全等于 1
      moves.push(src + '->' + dst); // 把 src 加 「 减 超过 」 加 dst 压入栈/数组尾部
      return moves; // 返回 moves
    }
    hanoi(n - 1, src, dst, aux, moves); // hanoi(元素个数 减 1, src, dst, aux, moves);
    moves.push(src + '->' + dst); // 把 src 加 「 减 超过 」 加 dst 压入栈/数组尾部
    hanoi(n - 1, aux, src, dst, moves); // hanoi(元素个数 减 1, aux, src, dst, moves);
    return moves; // 返回 moves
  }

  function eqArr(a: string[], b: string[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { n: number; want: string[] }[] = [
    {
      n: 3,
      want: ['A->C', 'A->B', 'C->B', 'A->C', 'B->A', 'B->C', 'A->C'],
    },
    { n: 1, want: ['A->C'] },
    { n: 2, want: ['A->B', 'A->C', 'B->C'] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = hanoi(c.n, 'A', 'B', 'C'); // 把 hanoi(字符.元素个数, 「A」, 「A」, 「A」) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL hanoi(%d)=%o want %o', c.n, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
