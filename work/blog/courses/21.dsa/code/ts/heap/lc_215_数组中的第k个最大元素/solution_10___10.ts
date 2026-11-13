// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// Faithful translation of python reference. Self-check via demo().
function find_kth_largest(nums: number[], k: number): number {
  // 定义函数/方法 find_kth_largest
  let lo = nums[0],
    hi = nums[0]; // 把 数组[0], 右边界 赋值为 数组[0] 存入 左边界
  for (const x of nums) {
    if (x < lo) lo = x;
    if (x > hi) hi = x;
  }
  const count = new Array(hi - lo + 1).fill(0); // 把 new Array(右边界 减 左边界 加 1).fill(0) 存入 计数
  for (const x of nums) count[x - lo]++; // for (const x of 数组) 计数[x 减 左边界] 加一 ;
  let remaining = k; // 把 下标 k 存入 remaining
  for (let v = hi; v >= lo; v--) {
    // 让 值 从 右边界 开始计数，值 不低于 左边界 就继续
    remaining -= count[v - lo]; // remaining累减 计数[值 减 左边界]
    if (remaining <= 0) return v; // 若 remaining 不超过 0，直接返回 值
  }
  return lo; // 返回 左边界
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    [[3, 2, 1, 5, 6, 4], 2],
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
  ];
  const want = [5, 4]; // 把 [5, 4] 存入 want
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = find_kth_largest(cases[i][0].slice(), cases[i][1]);
    if (got !== want[i])
      throw new Error('FAIL case ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
