/**
 * LeetCode 621. 任务调度器
 * 方案：方案4（26 位频率桶公式法）
 * 来源：https://blog.csdn.net/tyro_java/article/details/130482987
 * 忠实翻译 python/queue/lc_621_任务调度器/solution_4___4.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function leastInterval(tasks: string[], n: number): number {
    // 定义函数/方法 leastInterval
    const freq: number[] = new Array(26).fill(0); // 把 new Array(26).fill(0); 写入 const freq: number[]
    for (const t of tasks) {
      // for (const 另一字符串 of tasks) {
      freq[t.charCodeAt(0) - 'A'.charCodeAt(0)]++; // 频次表[另一字符串.charCodeAt(0) 减 「A」.charCodeAt(0)] 加一 ;
    }
    let maxFreq = 0; // 把 0 存入 maxFreq
    for (const f of freq) {
      // for (const f of 频次表) {
      if (f > maxFreq) maxFreq = f; // 若 f 超过 maxFreq) maxFreq 赋值为 f;
    }
    let same = 0; // 把 0 存入 same
    for (const f of freq) {
      // for (const f of 频次表) {
      if (f === maxFreq) same++; // 若 f 全等于 maxFreq) same 加一 ;
    }
    return Math.max((maxFreq - 1) * (n + 1) + same, tasks.length); // 返回 Math.取较大值 (maxFreq 减 1) 乘 (元素个数 加 1) 加 same, tasks.长度)
  }

  const cases: { tasks: string[]; n: number; want: number }[] = [
    { tasks: ['A', 'A', 'A', 'B', 'B', 'B'], n: 2, want: 8 },
    { tasks: ['A', 'A', 'A', 'A'], n: 2, want: 10 },
    { tasks: ['A', 'B', 'C', 'D'], n: 0, want: 4 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = leastInterval(c.tasks, c.n); // 把 leastInterval(字符.tasks, 字符.元素个数) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL leastInterval(%o,%d)=%d want %d',
        c.tasks,
        c.n,
        got,
        c.want,
      ); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
