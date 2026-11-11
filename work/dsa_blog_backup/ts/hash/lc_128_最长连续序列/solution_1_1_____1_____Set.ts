// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144830623
/** 来源: LeetCode 128 最长连续序列 */
export function longestConsecutive(nums: number[]): number {
  // 定义函数/方法 longestConsecutive
  const set = new Set(nums); // 把 new Set(数组) 存入 set
  let best = 0; // 把 0 存入 当前最优
  for (const num of set) {
    // for (const num of set) {
    if (!set.has(num - 1)) {
      // 若 取反 set.has(num 减 1
      let cur = num,
        streak = 1; // 把 num, streak 赋值为 1 存入 当前值
      while (set.has(cur + 1)) {
        cur++;
        streak++;
      } // 循环，直到不满足「set.has(当前值 加 1)) { 当前值 加一 ; streak 加一 ; }」
      if (streak > best) best = streak; // 若 streak 超过 当前最优) 当前最优 赋值为 streak;
    }
  }
  return best; // 返回 当前最优
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number][] = [
    [[100, 4, 200, 1, 3, 2], 4],
    [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
    [[1, 0, 1, 2], 3],
  ];
  for (const [inp, want] of cases) {
    // for (const [inp, want] of cases) {
    const got = longestConsecutive(inp); // 把 longestConsecutive(inp) 存入 got
    if (got !== want)
      throw new Error(`FAIL in=${JSON.stringify(inp)} want=${want} got=${got}`);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
