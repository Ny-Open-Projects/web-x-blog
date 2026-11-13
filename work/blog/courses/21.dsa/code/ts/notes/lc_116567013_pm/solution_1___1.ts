/**
 * LeetCode 116567013. PM
 * 来源：https://blog.csdn.net/tyro_java/article/details/116567013
 * 忠实翻译 python/notes/lc_116567013_pm/solution_1___1.py
 */

// Brute-Force 模式匹配（版本1：主串指针回退）。
// 返回模式 P 在文本 T 中首次出现的起始下标，未找到返回 -1。
function matchV1(P: string, T: string): number {
  // 定义函数/方法 matchV1
  const n = T.length; // 把 T.长度 存入 元素个数
  const m = P.length; // 把 P.长度 存入 映射表
  let i = 0; // 把 0 存入 下标 i
  let j = 0; // 把 0 存入 下标 j
  while (j < m && i < n) {
    // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
    if (T[i] === P[j]) {
      // 若 T[下标 i] 全等于 P[下标 j]
      i += 1; // 下标 i累加 1
      j += 1; // 下标 j累加 1
    } else {
      // 否则
      i -= j - 1; // 主串回退到本次对齐的下一位置
      j = 0; // 把 0 存入 下标 j
    }
  }
  return j === m ? i - j : -1; // 返回 下标 j 全等于 映射表 ? 下标 i 减 下标 j : 减 1
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const T = 'now is the time for all good people to come'; // 把 'now is the time for all good people to come' 存入 T
  const cases: { p: string; T: string; want: number }[] = [
    { p: 'people', T: T, want: 29 },
    { p: 'good', T: T, want: 24 },
    { p: 'no', T: T, want: 0 },
    { p: 'xyz', T: T, want: -1 }, // 未命中
    { p: 'a', T: '', want: -1 }, // 边界：空文本
    { p: 'good', T: 'good', want: 0 }, // 边界：文本恰为模式
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = matchV1(c.p, c.T); // 把 matchV1(字符.节点, 字符.T) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL match_v1("' + c.p + '")=' + got + ' want ' + c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
