// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
/**
 ** LeetCode 209. 长度最小的子数组
 ** 方案4: 滑动窗口
 */

function minSubArrayLen(target: number, nums: number[]): number {
  // 定义函数/方法 minSubArrayLen
  const n = nums.length; // 把 数组.长度 存入 元素个数
  let slow = 0,
    fast = 0,
    total = 0; // 把 0, 快指针 赋值为 0, 总和 赋值为 0 存入 慢指针
  let result = n + 1; // 把 元素个数 加 1 存入 结果
  while (fast < n) {
    // 循环，直到不满足「快指针 小于 元素个数」
    total += nums[fast]; // 总和累加 数组[快指针]
    while (total >= target) {
      // 循环，直到不满足「总和 不低于 目标值」
      result = Math.min(result, fast - slow + 1); // 把 Math.取较小值 结果, 快指针 减 慢指针 加 1) 存入 结果
      total -= nums[slow]; // 总和累减 数组[慢指针]
      slow += 1; // 慢指针累加 1
    }
    fast += 1; // 快指针累加 1
  }
  return result <= n ? result : 0; // 返回 结果 不超过 元素个数 ? 结果 : 0
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { in: [number, number[]]; want: number }[] = [
    { in: [1, [1, 2, 3]], want: 1 },
    { in: [7, [2, 3, 1, 2, 4, 3]], want: 2 },
    { in: [11, [1, 1, 1, 1, 1, 1, 1, 1]], want: 0 },
    { in: [4, [1, 4, 4]], want: 1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = minSubArrayLen(c.in[0], c.in[1]); // 把 minSubArrayLen(字符.in[0], 字符.in[1]) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL minSubArrayLen(' +
          c.in[0] +
          ',' +
          JSON.stringify(c.in[1]) +
          ')=' +
          got +
          ' want ' +
          c.want,
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
