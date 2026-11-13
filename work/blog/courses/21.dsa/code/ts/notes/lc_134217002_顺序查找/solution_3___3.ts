// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function seq_search(nums: number[], target: number): number {
  // 定义函数/方法 seq_search
  for (let i = 0; i < nums.length; i++) if (nums[i] === target) return i; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
  return -1; // 返回 减 1
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number, number][] = [
    [[15, 4, 23, 52, 1], 23, 2],
    [[15, 4, 23, 52, 1], 123, -1],
    [[1, 2, 3, 4, 5], 3, 2],
    [[1, 2, 3, 4, 5], 6, -1],
    [[10, 20, 30, 40, 50], 10, 0],
    [[10, 20, 30, 40, 50], 50, 4],
    [[], 1, -1],
    [[1], 1, 0],
    [[1], 2, -1],
  ];
  for (const [nums, target, expected] of cases) {
    // for (const [数组, 目标值, expected] of cases) {
    assertEq(
      seq_search(nums, target),
      expected,
      'case ' + JSON.stringify(nums) + ' ' + target,
    ); // 断言校验
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
