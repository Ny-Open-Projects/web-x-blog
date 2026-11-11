// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345965
/**
 ** LeetCode 384. 打乱数组
 ** 方案1: Fisher-Yates（从后往前）
 */

class Solution {
  // 定义类型
  private nums: number[]; // private 数组: number[];
  private original: number[]; // private original: number[];

  constructor(nums: number[]) {
    // constructor(数组: number[]) {
    this.nums = [...nums]; // 把 复制的 数组 ; 写入 数组
    this.original = [...nums]; // 把 复制的 数组 ; 写入 this.original
  }

  reset(): number[] {
    // reset(): number[] {
    this.nums = [...this.original]; // 把 [...this.original]; 写入 数组
    return this.nums; // 返回 this.数组
  }

  shuffle(): number[] {
    // shuffle(): number[] {
    const shuffled = [...this.nums]; // 把 [...this.数组] 存入 shuffled
    for (let i = shuffled.length - 1; i > 0; i--) {
      // 让 下标 i 从 shuffled.长度 减 1 开始计数，下标 i 超过 0 就继续
      const j = Math.floor(Math.random() * (i + 1)); // 把 向下取整(Math.random() 乘 (下标 i 加 1)) 存入 下标 j
      const tmp = shuffled[i]; // 把 shuffled[下标 i] 存入 临时变量
      shuffled[i] = shuffled[j]; // 把 shuffled[下标 j]; 写入 shuffled[i]
      shuffled[j] = tmp; // 把 临时变量; 写入 shuffled[j]
    }
    this.nums = shuffled; // 把 shuffled; 写入 数组
    return this.nums; // 返回 this.数组
  }
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  let fail = false; // 把 false 存入 fail
  const sol = new Solution([1, 2, 3]); // 把 new Solution([1, 2, 3]) 存入 sol
  const sh = sol.shuffle(); // 把 sol.shuffle() 存入 sh
  const sorted = [...sh].sort((a, b) => a - b);
  if (JSON.stringify(sorted) !== JSON.stringify([1, 2, 3])) {
    // 若 JSON.stringify(sorted) 不等于 JSON.stringify([1, 2, 3]
    fail = true; // 把 true 存入 fail
    console.log('FAIL shuffle not a permutation: ' + JSON.stringify(sh)); // 打印输出
  }
  const rs = sol.reset(); // 把 sol.reset() 存入 rs
  if (JSON.stringify(rs) !== JSON.stringify([1, 2, 3])) {
    // 若 JSON.stringify(rs) 不等于 JSON.stringify([1, 2, 3]
    fail = true; // 把 true 存入 fail
    console.log('FAIL reset=' + JSON.stringify(rs)); // 打印输出
  }
  const sol2 = new Solution([5]); // 把 new Solution([5]) 存入 sol2
  if (JSON.stringify(sol2.shuffle()) !== JSON.stringify([5])) {
    // 若 JSON.stringify(sol2.shuffle()) 不等于 JSON.stringify([5]
    fail = true; // 把 true 存入 fail
    console.log('FAIL single-element shuffle'); // 打印输出
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
