// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function findLengthOfLCIS(nums: number[]): number {
    // 定义函数/方法 findLengthOfLCIS
    if (nums.length === 0) {
      // 若 数组.长度 全等于 0
      return 0; // 返回 0
    }
    let ans = 1; // 把 1 存入 答案
    let cur = 1; // 把 1 存入 当前值
    for (let i = 1; i < nums.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] > nums[i - 1]) {
        // 若 数组[下标 i] 超过 数组[下标 i 减 1]
        cur += 1; // 当前值累加 1
        ans = Math.max(ans, cur); // 把 Math.取较大值 答案, 当前值) 存入 答案
      } else {
        // 否则
        cur = 1; // 把 1 存入 当前值
      }
    }
    return ans; // 返回 答案
  }

  const cases: { in: number[]; want: number }[] = [
    { in: [2, 2, 2, 2, 2], want: 1 },
    { in: [1, 3, 5, 4, 7], want: 3 },
    { in: [], want: 0 },
    { in: [5], want: 1 },
    { in: [1, 2, 3, 2, 3, 4, 5], want: 4 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = findLengthOfLCIS(c.in); // 把 findLengthOfLCIS(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL findLengthOfLCIS(%o)=%d want %d', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
