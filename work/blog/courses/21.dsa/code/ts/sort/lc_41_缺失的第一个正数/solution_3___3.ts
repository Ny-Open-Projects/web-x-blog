/**
 ** LeetCode 41. 缺失的第一个正数
 ** 方案：方案3
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134429994
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function firstMissingPositive(nums: number[]): number {
    // 定义函数/方法 firstMissingPositive
    if (nums.length === 0) return 1; // 若 数组.长度 全等于 0，直接返回 1
    const pos = nums.filter((item) => item > 0);
    if (pos.length === 0) return 1; // 若 pos.长度 全等于 0，直接返回 1
    pos.sort((a, b) => a - b);
    if (pos[0] !== 1) return 1; // 若 pos[0] 不等于 1，直接返回 1
    const n = pos.length; // 把 pos.长度 存入 元素个数
    for (let i = 0; i < n - 1; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
      if (pos[i + 1] - pos[i] > 1) {
        // 若 pos[下标 i 加 1] 减 pos[下标 i] 超过 1
        return pos[i] + 1; // 返回 pos[下标 i] 加 1
      }
    }
    return pos[n - 1] + 1; // 返回 pos[元素个数 减 1] 加 1
  }
  const cases: Array<{ nums: number[]; want: number }> = [
    { nums: [1, 2, 0], want: 3 },
    { nums: [3, 4, -1, 1], want: 2 },
    { nums: [7, 8, 9, 11, 12], want: 1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = firstMissingPositive(c.nums); // 把 firstMissingPositive(字符.数组) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      console.log(
        `FAIL firstMissingPositive(${JSON.stringify(c.nums)})=${got} want ${c.want}`,
      );
      fail = true; // 把 true 存入 fail
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
