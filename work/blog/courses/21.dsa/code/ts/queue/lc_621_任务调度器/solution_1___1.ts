/**
 * LeetCode 621. 任务调度器
 * 方案：方案1（Counter 公式法）
 * 来源：https://blog.csdn.net/tyro_java/article/details/130482987
 * 忠实翻译 python/queue/lc_621_任务调度器/solution_1___1.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function leastInterval(tasks: string[], n: number): number {
    // 定义函数/方法 leastInterval
    const count: Record<string, number> = {}; // 把 {}; 写入 const count: Record<string, number>
    for (const t of tasks) {
      // for (const 另一字符串 of tasks) {
      count[t] = (count[t] === undefined ? 0 : count[t]) + 1; // 把 (计数[另一字符串] 全等于 undefined ? 0 : 计数[另一字符串]) 加 1; 写入 count[t]
    }
    let maxCount = 0; // 把 0 存入 maxCount
    for (const k in count) {
      // for (const 下标 k in 计数) {
      if (count[k] > maxCount) maxCount = count[k]; // 若 计数[下标 k] 超过 maxCount) maxCount 赋值为 计数[下标 k];
    }
    let maxCountTasks = 0; // 把 0 存入 maxCountTasks
    for (const k in count) {
      // for (const 下标 k in 计数) {
      if (count[k] === maxCount) maxCountTasks++; // 若 计数[下标 k] 全等于 maxCount) maxCountTasks 加一 ;
    }
    return Math.max(tasks.length, (maxCount - 1) * (n + 1) + maxCountTasks);
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
