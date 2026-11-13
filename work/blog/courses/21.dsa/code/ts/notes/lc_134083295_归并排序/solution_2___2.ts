// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function mergeSort(nums: number[]): number[] {
  // 定义函数/方法 mergeSort
  if (nums.length <= 1) return nums.slice(); // 若 数组.长度 不超过 1，直接返回 数组 截取 )
  const mid = Math.floor(nums.length / 2); // 把 向下取整(数组.长度 除以 2) 存入 中点
  const left = mergeSort(nums.slice(0, mid)); // 把 mergeSort(数组 截取 0, 中点)) 存入 左边界
  const right = mergeSort(nums.slice(mid)); // 把 mergeSort(数组 截取 中点)) 存入 右边界
  return merge(left, right); // 返回 merge(左边界, 右边界)
}
function merge(left: number[], right: number[]): number[] {
  // 定义函数/方法 merge
  const result: number[] = [];
  let i = 0,
    j = 0; // 把 []; let 下标 i 赋值为 0, 下标 j 赋值为 0; 写入 const result: number[]
  while (i < left.length && j < right.length) {
    // 循环，直到不满足「下标 i 小于 左边界.长度 且 下标 j 小于 右边界.长度」
    if (left[i] <= right[j]) result.push(left[i++]);
    else result.push(right[j++]);
  }
  while (i < left.length) result.push(left[i++]); // 循环，直到不满足「下标 i 小于 左边界.长度) 结果 追加 左边界[下标 i 加一 ]);」
  while (j < right.length) result.push(right[j++]); // 循环，直到不满足「下标 j 小于 右边界.长度) 结果 追加 右边界[下标 j 加一 ]);」
  return result; // 返回 结果
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(mergeSort([1, 2, 3]), [1, 2, 3], 'sorted'); // 断言校验
  assertEq(mergeSort([3, 1, 2]), [1, 2, 3], 'unsorted'); // 断言校验
  assertEq(mergeSort([]), [], 'empty'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
