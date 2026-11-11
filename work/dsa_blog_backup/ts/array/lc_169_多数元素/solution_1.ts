/**
 ** LeetCode 169. 多数元素
 ** 方案：1 ) 方案1：哈希计数取最大值
 */

// 忠实翻译 Python 参考实现 ref_majorityElement：Counter(nums).most_common(1)[0][0]
function majorityElement(nums: number[]): number {
  // 定义函数/方法 majorityElement
  const cnt: Record<number, number> = {}; // 把 {}; 写入 const cnt: Record<number, number>
  for (const v of nums) {
    // for (const 值 of 数组) {
    cnt[v] = (cnt[v] ?? 0) + 1; // 把 (计数[值] ?? 0) 加 1; 写入 cnt[v]
  }
  let best = 0; // 把 0 存入 当前最优
  let bestCnt = -1; // 把 减 1 存入 bestCnt
  for (const key in cnt) {
    // for (const key in 计数) {
    if (cnt[key] > bestCnt) {
      // 若 计数[key] 超过 bestCnt
      best = Number(key); // 把 Number(key) 存入 当前最优
      bestCnt = cnt[key]; // 把 计数[key] 存入 bestCnt
    }
  }
  return best; // 返回 当前最优
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 用例来自 _tools/correctness_check.py PROBLEMS["lc_169_多数元素"]
  const cases: [number[], number][] = [
    [[3, 2, 3], 3],
    [[2, 2, 1, 1, 1, 2, 2], 2],
    [[1], 1],
  ];
  for (const [input, want] of cases) {
    // for (const [input, want] of cases) {
    const got = majorityElement(input); // 把 majorityElement(input) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(
        `FAIL majorityElement(${JSON.stringify(input)}) = ${got}, want ${want}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
