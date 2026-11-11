// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831173
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function longestArithSeqLength(nums: number[]): number {
    // 定义函数/方法 longestArithSeqLength
    if (nums.length <= 2) return nums.length; // 若 数组.长度 不超过 2，直接返回 数组.长度
    const n = nums.length; // 把 数组.长度 存入 元素个数
    const dp: { [d: number]: number }[] = []; // 把 []; 写入 const dp: { [d: number]: number }[]
    for (let i = 0; i < n; i++) dp.push({}); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    let ans = 2; // 把 2 存入 答案
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (let j = 0; j < i; j++) {
        // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        const d = nums[i] - nums[j]; // 把 数组[下标 i] 减 数组[下标 j] 存入 d
        const prev = dp[j][d] === undefined ? 1 : dp[j][d]; // 把 DP 表[下标 j][d] 全等于 undefined ? 1 : DP 表[下标 j][d] 存入 前一个
        const cur = prev + 1; // 把 前一个 加 1 存入 当前值
        dp[i][d] = cur; // 把 当前值; 写入 dp[i][d]
        if (cur > ans) ans = cur; // 若 当前值 超过 答案) 答案 赋值为 当前值;
      }
    }
    return ans; // 返回 答案
  }

  const cases: { in: number[]; want: number }[] = [
    { in: [9, 4, 7, 2, 10], want: 3 },
    { in: [3, 6, 9, 12], want: 4 },
    { in: [20, 1, 15, 3, 10, 5, 8], want: 4 },
    { in: [1], want: 1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = longestArithSeqLength(c.in); // 把 longestArithSeqLength(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL in=' + JSON.stringify(c.in) + ' got=' + got + ' want=' + c.want,
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
