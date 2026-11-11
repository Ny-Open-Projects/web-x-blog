// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function longestMonotonicSubarray(nums: number[]): number {
  // 定义函数/方法 longestMonotonicSubarray
  if (!nums.length) return 0; // 若 取反 数组.长度，直接返回 0
  const n = nums.length;
  let ans = 1;
  let i = 0; // 把 数组.长度; let 答案 赋值为 1; let 下标 i 赋值为 0 存入 元素个数
  while (i < n) {
    // 循环，直到不满足「下标 i 小于 元素个数」
    let j = i; // 把 下标 i 存入 下标 j
    while (j + 1 < n && nums[j + 1] > nums[j]) j++;
    ans = Math.max(ans, j - i + 1); // 把 Math.取较大值 答案, 下标 j 减 下标 i 加 1) 存入 答案
    j = i; // 把 下标 i 存入 下标 j
    while (j + 1 < n && nums[j + 1] < nums[j]) j++;
    ans = Math.max(ans, j - i + 1); // 把 Math.取较大值 答案, 下标 j 减 下标 i 加 1) 存入 答案
    i++; // 下标 i 加一
  }
  return ans; // 返回 答案
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(longestMonotonicSubarray([1, 4, 3, 3, 2]), 2, 'lms'); // 断言校验
  assertEq(longestMonotonicSubarray([]), 0, 'empty'); // 断言校验
  assertEq(longestMonotonicSubarray([1, 2, 3, 4]), 4, 'inc'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
