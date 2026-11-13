// 丢失的数字：高斯求和 - 总和差值
// 忠实翻译 Python ref_missingNumber: n*(n+1)//2 - sum(nums)

function missingNumber(nums: number[]): number {
  // 定义函数/方法 missingNumber
  const n = nums.length; // 把 数组.长度 存入 元素个数
  let sum = 0; // 把 0 存入 累计和
  for (const v of nums) sum += v; // 把 值; 写入 for (const v of nums) sum +
  return (n * (n + 1)) / 2 - sum; // 返回 (元素个数 乘 (元素个数 加 1)) 除以 2 减 累计和
}

// 自检用例：(nums, 期望)
const cases: [number[], number][] = [
  [[3, 0, 1], 2],
  [[0, 1], 2],
  [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
];

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  for (const [nums, want] of cases) {
    // for (const [数组, want] of cases) {
    const got = missingNumber(nums); // 把 missingNumber(数组) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(
        `FAIL: missingNumber(${JSON.stringify(nums)})=${got} want ${want}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
