/**
 ** LeetCode 66. 加一
 ** 方案：1 ) 方案1：末位进位
 */

// 忠实翻译 Python 参考实现 ref_plusOne。
function plusOne(digits: number[]): number[] {
  // 定义函数/方法 plusOne
  const d = digits.slice(); // 把 digits 截取 ) 存入 d
  for (let i = d.length - 1; i >= 0; i--) {
    // 让 下标 i 从 d.长度 减 1 开始计数，下标 i 不低于 0 就继续
    if (d[i] === 9) {
      // 若 d[下标 i] 全等于 9
      d[i] = 0; // 把 0; 写入 d[i]
    } else {
      // 否则
      d[i]++; // d[下标 i] 加一 ;
      return d; // 返回 d
    }
  }
  const res: number[] = new Array(digits.length + 1).fill(0); // 把 new Array(digits.长度 加 1).fill(0); 写入 const res: number[]
  res[0] = 1; // 把 1; 写入 res[0]
  return res; // 返回 结果
}

function eqArr(a: number[], b: number[]): boolean {
  // 定义函数/方法 eqArr
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] !== b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 用例来自 _tools/correctness_check.py PROBLEMS["lc_66_加一"]
  const cases: [number[], number[]][] = [
    [
      [1, 2, 3],
      [1, 2, 4],
    ],
    [
      [4, 3, 2, 1],
      [4, 3, 2, 2],
    ],
    [
      [9, 9, 9],
      [1, 0, 0, 0],
    ],
  ];
  for (const [input, want] of cases) {
    // for (const [input, want] of cases) {
    const got = plusOne(input); // 把 plusOne(input) 存入 got
    if (!eqArr(got, want)) {
      // 若 取反 eqArr(got, want
      throw new Error(
        `FAIL plusOne(${JSON.stringify(input)}) = ${JSON.stringify(got)}, want ${JSON.stringify(want)}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
