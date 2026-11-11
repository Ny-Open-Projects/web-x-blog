// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function removeElement(nums: number[], val: number): number {
  // 定义函数/方法 removeElement
  let left = 0,
    right = nums.length - 1; // 把 0, 右边界 赋值为 数组.长度 减 1 存入 左边界
  while (left <= right) {
    // 循环，直到不满足「左边界 不超过 右边界」
    if (nums[left] === val) {
      nums[left] = nums[right];
      right--;
    } // 若 数组[左边界] 全等于 值) { 数组[左边界] 赋值为 数组[右边界]; 右边界 减一 ; }
    else left++; // 否则
  }
  return left; // 返回 左边界
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(removeElement([1, 2, 3], 1), 2, 're'); // 断言校验
  assertEq(removeElement([2, 2], 2), 0, 'all'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
