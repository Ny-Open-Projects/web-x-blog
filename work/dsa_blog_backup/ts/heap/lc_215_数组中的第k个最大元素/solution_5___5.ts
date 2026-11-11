// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// Faithful translation of python reference. Self-check via demo().
function findKthLargest(nums: number[], k: number): number {
  // 定义函数/方法 findKthLargest
  const a = nums.slice().sort((x, y) => y - x);
  return a.slice(0, k)[k - 1]; // 返回 数组 截取 0, 下标 k)[下标 k 减 1]
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
    const got = findKthLargest(cases[i][0].slice(), cases[i][1]); // 把 findKthLargest(cases[下标 i][0] 截取 ), cases[下标 i][1]) 存入 got
    if (got !== want[i])
      throw new Error('FAIL case ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
