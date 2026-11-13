/**
 * LeetCode 116567013. PM
 * 来源：https://blog.csdn.net/tyro_java/article/details/116567013
 * 忠实翻译 python/notes/lc_116567013_pm/solution_4___4.py
 */

// 构造 KMP 的 next 表（单独呈现，对应 C++ buildNext）。
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
  const cases: { p: string; want: number[] }[] = [
    { p: 'ababaca', want: [-1, 0, 0, 1, 2, 3, 0] },
    { p: 'aaaa', want: [-1, 0, 1, 2] },
    { p: 'abcabc', want: [-1, 0, 0, 0, 1, 2] },
    { p: 'abcd', want: [-1, 0, 0, 0] }, // 边界：无重复
    { p: 'a', want: [-1] }, // 边界：长度 1
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
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
