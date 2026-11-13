// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function findLengthOfLCIS(nums: number[]): number {
    // 定义函数/方法 findLengthOfLCIS
    if (nums.length === 0) return 0; // 若 数组.长度 全等于 0，直接返回 0
    let best = 1,
      cur = 1; // 把 1, 当前值 赋值为 1 存入 当前最优
    for (let i = 1; i < nums.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] > nums[i - 1]) cur++;
      else cur = 1; // 若 数组[下标 i] 超过 数组[下标 i 减 1]) 当前值 加一 ; else 当前值 赋值为 1;
      if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
    }
    return best; // 返回 当前最优
  }
  const cases = [
    { in: [1, 3, 5, 4, 7], want: 3 },
    { in: [2, 2, 2, 2, 2], want: 1 },
    { in: [1, 3, 5], want: 3 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = findLengthOfLCIS(c.in); // 把 findLengthOfLCIS(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
