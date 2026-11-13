/**
 * LeetCode 116567013. PM
 * 来源：https://blog.csdn.net/tyro_java/article/details/116567013
 * 忠实翻译 python/notes/lc_116567013_pm/solution_3___3.py
 */

// 构造 KMP 的 next 失效函数（look-up table）。
function buildNext(P: string): number[] {
  // 定义函数/方法 buildNext
  const m = P.length; // 把 P.长度 存入 映射表
  const N: number[] = new Array(m).fill(-1); // 把 new Array(映射表).fill( 减 1); 写入 const N: number[]
  let j = 0; // 把 0 存入 下标 j
  let t = -1; // 把 减 1 存入 另一字符串
  while (j < m - 1) {
    // 循环，直到不满足「下标 j 小于 映射表 减 1」
    if (t < 0 || P[j] === P[t]) {
      // 若 另一字符串 小于 0 或 P[下标 j] 全等于 P[另一字符串]
      j += 1; // 下标 j累加 1
      t += 1; // 另一字符串累加 1
      N[j] = t; // 把 另一字符串; 写入 N[j]
    } else {
      // 否则
      t = N[t]; // 把 N[另一字符串] 存入 另一字符串
    }
  }
  return N; // 返回 N
}

// KMP 模式匹配：借助 next 表在失配时大步跳跃，最坏 O(n)。
function kmpMatch(P: string, T: string): number {
  // 定义函数/方法 kmpMatch
  const N = buildNext(P); // 把 buildNext(P) 存入 N
  const n = T.length; // 把 T.长度 存入 元素个数
  const m = P.length; // 把 P.长度 存入 映射表
  let i = 0; // 把 0 存入 下标 i
  let j = 0; // 把 0 存入 下标 j
  while (j < m && i < n) {
    // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
    if (j < 0 || T[i] === P[j]) {
      // 若 下标 j 小于 0 或 T[下标 i] 全等于 P[下标 j]
      i += 1; // 下标 i累加 1
      j += 1; // 下标 j累加 1
    } else {
      // 否则
      j = N[j]; // 把 N[下标 j] 存入 下标 j
    }
  }
  return j === m ? i - j : -1; // 返回 下标 j 全等于 映射表 ? 下标 i 减 下标 j : 减 1
}

function eqArr(a: number[], b: number[]): boolean {
  // 定义函数/方法 eqArr
  if (a.length !== b.length) {
    // 若 数组.长度 不等于 b.长度
    return false; // 返回 false
  }
  for (let idx = 0; idx < a.length; idx += 1) {
    // 让 idx 从 0 开始计数，idx 小于 数组.长度 就继续
    if (a[idx] !== b[idx]) {
      // 若 数组[idx] 不等于 b[idx]
      return false; // 返回 false
    }
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const T = 'now is the time for all good people to come'; // 把 'now is the time for all good people to come' 存入 T
  const cases: { p: string; T: string; want: number }[] = [
    { p: 'people', T: T, want: 29 },
    { p: 'all', T: T, want: 20 },
    { p: 'no', T: T, want: 0 },
    { p: 'xyz', T: T, want: -1 }, // 未命中
    { p: 'a', T: '', want: -1 }, // 边界：空文本
    { p: 'aaaa', T: 'aaaaa', want: 0 }, // 边界：重叠前缀
    { p: 'aaab', T: 'aaabaaa', want: 0 }, // 边界：回退复用
  ];
  const tableCases: { p: string; want: number[] }[] = [
    { p: 'ababaca', want: [-1, 0, 0, 1, 2, 3, 0] },
    { p: 'aaaa', want: [-1, 0, 1, 2] },
    { p: 'abcd', want: [-1, 0, 0, 0] }, // 边界：无重复
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = kmpMatch(c.p, c.T); // 把 kmpMatch(字符.节点, 字符.T) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL kmp_match("' + c.p + '")=' + got + ' want ' + c.want); // 打印输出
    }
  }
  for (const c of tableCases) {
    // for (const 字符 of tableCases) {
    const got = buildNext(c.p); // 把 buildNext(字符.节点) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL build_next("' +
          c.p +
          ')=' +
          JSON.stringify(got) +
          ' want ' +
          JSON.stringify(c.want),
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
