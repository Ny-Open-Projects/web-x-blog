// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function rob(nums: number[]): number {
    // 定义函数/方法 rob
    const length = nums.length; // 把 数组.长度 存入 长度
    if (length === 0) return 0; // 若 长度 全等于 0，直接返回 0
    if (length === 1) return nums[0]; // 若 长度 全等于 1，直接返回 数组[0]
    function robRange(start: number, end: number): number {
      // 定义函数/方法 robRange
      if (end === start) return nums[start]; // 若 终点 全等于 起点，直接返回 数组[起点]
      const dp = new Array(end + 1).fill(0); // 把 new Array(终点 加 1).fill(0) 存入 DP 表
      dp[start] = nums[start]; // 把 数组[起点]; 写入 dp[start]
      dp[start + 1] = Math.max(nums[start], nums[start + 1]); // 把 Math.取较大值 数组[起点], 数组[起点 加 1]); 写入 dp[start + 1]
      for (let i = start + 2; i <= end; i++)
        dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]); // 让 下标 i 从 起点 加 2 开始计数，下标 i 不超过 终点 就继续
      return dp[end]; // 返回 DP 表[终点]
    }
    return Math.max(robRange(0, length - 2), robRange(1, length - 1)); // 返回 Math.取较大值 robRange(0, 长度 减 2), robRange(1, 长度 减 1))
  }
  const cases = [
    { in: [2, 3, 2], want: 3 },
    { in: [1, 2, 3, 1], want: 4 },
    { in: [5], want: 5 },
    { in: [], want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = rob(c.in); // 把 rob(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log(
        'FAIL rob(' + JSON.stringify(c.in) + ')=' + got + ' want ' + c.want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
