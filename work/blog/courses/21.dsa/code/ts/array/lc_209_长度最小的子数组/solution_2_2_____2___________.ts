// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
/**
 ** LeetCode 209. 长度最小的子数组
 ** 方案2: 前缀和 + 二分查找
 */

function minSubArrayLen(target: number, nums: number[]): number {
  // 定义函数/方法 minSubArrayLen
  const n = nums.length; // 把 数组.长度 存入 元素个数
  if (n === 0) return 0; // 若 元素个数 全等于 0，直接返回 0
  let ans = Number.MAX_SAFE_INTEGER; // 把 Number.MAX_SAFE_INTEGER 存入 答案
  const sums: number[] = new Array(n + 1).fill(0); // 把 new Array(元素个数 加 1).fill(0); 写入 const sums: number[]
  for (let i = 1; i <= n; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
    sums[i] = sums[i - 1] + nums[i - 1]; // 把 sums[下标 i 减 1] 加 数组[下标 i 减 1]; 写入 sums[i]
  }
  for (let i = 1; i <= n; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
    const t = sums[i - 1] + target; // 把 sums[下标 i 减 1] 加 目标值 存入 另一字符串
    // bisect_left: 第一个满足 sums[idx] >= t 的下标
    let lo = 0,
      hi = n + 1; // 把 0, 右边界 赋值为 元素个数 加 1 存入 左边界
    while (lo < hi) {
      // 循环，直到不满足「左边界 小于 右边界」
      const mid = Math.floor((lo + hi) / 2); // 把 向下取整((左边界 加 右边界) 除以 2) 存入 中点
      if (sums[mid] < t) lo = mid + 1;
      else hi = mid; // 若 sums[中点] 小于 另一字符串) 左边界 赋值为 中点 加 1; else 右边界 赋值为 中点;
    }
    const bound = lo; // 把 左边界 存入 bound
    if (bound <= n) {
      // 若 bound 不超过 元素个数
      ans = Math.min(ans, bound - (i - 1)); // 把 Math.取较小值 答案, bound 减 (下标 i 减 1)) 存入 答案
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
