/**
 ** LeetCode 1. 两数之和
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133322239
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function twoSum(nums: number[], target: number): number[] {
    // 定义函数/方法 twoSum
    const n = nums.length; // 把 数组.长度 存入 元素个数
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (let j = i + 1; j < n; j++) {
        // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
        if (nums[i] + nums[j] === target) {
          // 若 数组[下标 i] 加 数组[下标 j] 全等于 目标值
          return [i, j]; // 返回 [下标 i, 下标 j]
        }
      }
    }
    return []; // 返回 []
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    const x = [...a].sort((p, q) => p - q);
    const y = [...b].sort((p, q) => p - q);
    for (let i = 0; i < x.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 x.长度 就继续
      if (x[i] !== y[i]) return false; // 若 x[下标 i] 不等于 y[下标 i]，直接返回 false
    }
    return true; // 返回 true
  }

  const cases: Array<{ nums: number[]; target: number; want: number[] }> = [
    { nums: [2, 7, 11, 15], target: 9, want: [0, 1] },
    { nums: [3, 2, 4], target: 6, want: [1, 2] },
    { nums: [3, 3], target: 6, want: [0, 1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = twoSum(c.nums, c.target); // 把 twoSum(字符.数组, 字符.目标值) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      console.log(
        `FAIL twoSum(${JSON.stringify(c.nums)},${c.target})=${JSON.stringify(got)} want ${JSON.stringify(c.want)}`,
      );
      fail = true; // 把 true 存入 fail
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
