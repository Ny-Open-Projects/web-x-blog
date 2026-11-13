/**
 * LeetCode 621. 任务调度器
 * 方案：方案5（公式法：出现最多的任务 freq 个，有 same 个并列最多，
 *        最少时间 = (freq-1)*(n+1) + same，且不能少于任务总数）
 * 来源：https://blog.csdn.net/tyro_java/article/details/130482987
 * 忠实翻译 python/queue/lc_621_任务调度器/solution_5___5.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function leastInterval(tasks: string[], n: number): number {
    // 定义函数/方法 leastInterval
    const cnt: Record<string, number> = {}; // 把 {}; 写入 const cnt: Record<string, number>
    for (const t of tasks) {
      // for (const 另一字符串 of tasks) {
      cnt[t] = (cnt[t] === undefined ? 0 : cnt[t]) + 1; // 把 (计数[另一字符串] 全等于 undefined ? 0 : 计数[另一字符串]) 加 1; 写入 cnt[t]
    }
    let freq = 0; // 把 0 存入 频次表
    for (const k in cnt) {
      // for (const 下标 k in 计数) {
      if (cnt[k] > freq) freq = cnt[k]; // 若 计数[下标 k] 超过 频次表) 频次表 赋值为 计数[下标 k];
    }
    let same = 0; // 把 0 存入 same
    for (const k in cnt) {
      // for (const 下标 k in 计数) {
      if (cnt[k] === freq) same++; // 若 计数[下标 k] 全等于 频次表) same 加一 ;
    }
    return Math.max((freq - 1) * (n + 1) + same, tasks.length); // 返回 Math.取较大值 (频次表 减 1) 乘 (元素个数 加 1) 加 same, tasks.长度)
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
