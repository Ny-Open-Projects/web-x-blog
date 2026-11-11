/**
 ** LeetCode 107490876. 计算思维之分书和八皇后问题
 ** 分书问题（基础回溯）：把 5 本书分给 A~E 五人，每人都分到自己感兴趣的书
 ** 来源：https://blog.csdn.net/tyro_java/article/details/107490876
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const like: number[][] = [
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
  ];
  const results: number[][] = []; // 把 []; 写入 const results: number[][]
  const assigned: number[] = [-1, -1, -1, -1, -1]; // 把 [ 减 1, 减 1, 减 1, 减 1, 减 1]; 写入 const assigned: number[]

  function tryAssign(reader: number): void {
    // 定义函数/方法 tryAssign
    if (reader === 5) {
      // 若 reader 全等于 5
      results.push(assigned.slice()); // 把 assigned 截取 压入栈/数组尾部
      return; // return;
    }
    for (let book = 0; book < 5; book++) {
      // 让 book 从 0 开始计数，book 小于 5 就继续
      if (like[reader][book] === 1 && assigned[book] === -1) {
        // 若 like[reader][book] 全等于 1 且 assigned[book] 全等于 减 1
        assigned[book] = reader; // 把 reader; 写入 assigned[book]
        tryAssign(reader + 1); // tryAssign(reader 加 1);
        assigned[book] = -1; // 回溯
      }
    }
  }

  function allocateBooks(): number[][] {
    // 定义函数/方法 allocateBooks
    tryAssign(0); // tryAssign(0);
    return results; // 返回 results
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const res = allocateBooks(); // 把 allocateBooks() 存入 结果
  const want: number[][] = [
    [1, 2, 0, 3, 4],
    [1, 4, 0, 3, 2],
  ];
  let fail = false; // 把 false 存入 fail
  if (res.length !== want.length) {
    // 若 结果.长度 不等于 want.长度
    fail = true; // 把 true 存入 fail
    console.log(
      'FAIL allocate_books count=' + res.length + ' want ' + want.length,
    ); // 打印输出
  } else {
    // 否则
    for (let i = 0; i < want.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
      if (!eqArr(res[i], want[i])) {
        // 若 取反 eqArr(结果[下标 i], want[下标 i]
        fail = true; // 把 true 存入 fail
        console.log(
          'FAIL allocate_books[' +
            i +
            ']=' +
            JSON.stringify(res[i]) +
            ' want ' +
            JSON.stringify(want[i]),
        ); // 打印输出
      }
    }
  }
  // 附加性质：每个方案都合法（每人拿到喜欢的书且书不重复）
  for (const scheme of res) {
    // for (const scheme of 结果) {
    const seen = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 已见集合
    for (let book = 0; book < 5; book++) {
      // 让 book 从 0 开始计数，book 小于 5 就继续
      const reader = scheme[book]; // 把 scheme[book] 存入 reader
      if (like[reader][book] !== 1 || seen.has(book)) {
        // 若 like[reader][book] 不等于 1 或 已见集合.has(book
        fail = true; // 把 true 存入 fail
        console.log('FAIL invalid scheme ' + JSON.stringify(scheme)); // 打印输出
      }
      seen.add(book); // 已见集合 追加 book);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
