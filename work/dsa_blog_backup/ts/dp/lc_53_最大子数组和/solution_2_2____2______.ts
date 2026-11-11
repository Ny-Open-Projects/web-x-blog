/**
 ** LeetCode 53. 最大子数组和
 ** 方案：2 ）方案2: 动态规划
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144847570
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function maxSubArray(nums: number[]): number {
    // 定义函数/方法 maxSubArray
    let best = nums[0]; // 把 数组[0] 存入 当前最优
    let cur = nums[0]; // 把 数组[0] 存入 当前值
    for (let i = 1; i < nums.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      cur = Math.max(nums[i], cur + nums[i]); // 把 Math.取较大值 数组[下标 i], 当前值 加 数组[下标 i]) 存入 当前值
      best = Math.max(best, cur); // 把 Math.取较大值 当前最优, 当前值) 存入 当前最优
    }
    return best; // 返回 当前最优
  }
  const cases: Array<{ nums: number[]; want: number }> = [
    { nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4], want: 6 },
    { nums: [1], want: 1 },
    { nums: [5, 4, -1, 7, 8], want: 23 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = maxSubArray(c.nums); // 把 maxSubArray(字符.数组) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      console.log(
        `FAIL maxSubArray(${JSON.stringify(c.nums)})=${got} want ${c.want}`,
      );
      fail = true; // 把 true 存入 fail
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
