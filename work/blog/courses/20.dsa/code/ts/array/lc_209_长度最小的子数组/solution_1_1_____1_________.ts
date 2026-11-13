// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
/**
 ** LeetCode 209. 长度最小的子数组
 ** 方案1: 暴力枚举
 */

function minSubArrayLen(target: number, nums: number[]): number {
  // 定义函数/方法 minSubArrayLen
  const n = nums.length; // 把 数组.长度 存入 元素个数
  if (n === 0) return 0; // 若 元素个数 全等于 0，直接返回 0
  let ans = Number.MAX_SAFE_INTEGER; // 把 Number.MAX_SAFE_INTEGER 存入 答案
  for (let i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    let sum = 0; // 把 0 存入 累计和
    for (let j = i; j < n; j++) {
      // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
      sum += nums[j]; // 累计和累加 数组[下标 j]
      if (sum >= target) {
        // 若 累计和 不低于 目标值
        ans = Math.min(ans, j - i + 1); // 把 Math.取较小值 答案, 下标 j 减 下标 i 加 1) 存入 答案
        break; // 跳出循环
      }
    }
  }
  return ans === Number.MAX_SAFE_INTEGER ? 0 : ans; // 返回 答案 全等于 Number.MAX_SAFE_INTEGER ? 0 : 答案
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
