/**
 * LeetCode 116567013. PM
 * 来源：https://blog.csdn.net/tyro_java/article/details/116567013
 * 忠实翻译 python/notes/lc_116567013_pm/solution_2___2.py
 */

// Brute-Force 模式匹配（版本2：双循环对齐）。
// 每次对齐后用内层循环逐字符比较。
function matchV2(P: string, T: string): number {
  // 定义函数/方法 matchV2
  const n = T.length; // 把 T.长度 存入 元素个数
  const m = P.length; // 把 P.长度 存入 映射表
  for (let i = 0; i <= n - m; i += 1) {
    // 让 下标 i 从 0 开始计数，下标 i 不超过 元素个数 减 映射表 就继续
    let j = 0; // 把 0 存入 下标 j
    while (j < m && T[i + j] === P[j]) {
      // 循环，直到不满足「下标 j 小于 映射表 且 T[下标 i 加 下标 j] 全等于 P[下标 j]」
      j += 1; // 下标 j累加 1
    }
    if (j === m) {
      // 若 下标 j 全等于 映射表
      return i; // 返回 下标 i
    }
  }
  return -1; // 返回 减 1
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const T = 'now is the time for all good people to come'; // 把 'now is the time for all good people to come' 存入 T
  const cases: { p: string; T: string; want: number }[] = [
    { p: 'people', T: T, want: 29 },
    { p: 'time', T: T, want: 11 },
    { p: 'all', T: T, want: 20 },
    { p: 'xyz', T: T, want: -1 }, // 未命中
    { p: 'a', T: '', want: -1 }, // 边界：空文本
    { p: 'is', T: 'is', want: 0 }, // 边界：文本恰为模式
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = matchV2(c.p, c.T); // 把 matchV2(字符.节点, 字符.T) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL match_v2("' + c.p + '")=' + got + ' want ' + c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
