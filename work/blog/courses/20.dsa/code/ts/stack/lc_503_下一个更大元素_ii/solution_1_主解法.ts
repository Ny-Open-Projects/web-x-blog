// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347297

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function nextGreaterElements(nums: number[]): number[] {
  // 定义函数/方法 nextGreaterElements
  const n = nums.length;
  const result = new Array(n).fill(-1);
  const stack: number[] = [];
  for (let i = 0; i < 2 * n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 2 乘 元素个数 就继续
    const num = nums[i % n]; // 把 数组[下标 i 对…取模 元素个数] 存入 num
    while (stack.length && nums[stack[stack.length - 1]] < num) {
      // 循环，直到不满足「栈.长度 且 数组[栈[栈.长度 减 1]] 小于 num」
      const idx = stack.pop()!;
      result[idx] = num; // 把 栈 弹出 )取反 ; 结果[idx] 赋值为 num 存入 idx
    }
    if (i < n) stack.push(i); // 若 下标 i 小于 元素个数) 栈 追加 下标 i);
  }
  return result; // 返回 结果
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(nextGreaterElements([1, 2, 1]), [2, -1, 2], 'nge'); // 断言校验
  assertEq(nextGreaterElements([3, 2, 1]), [-1, 3, 3], 'desc'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
