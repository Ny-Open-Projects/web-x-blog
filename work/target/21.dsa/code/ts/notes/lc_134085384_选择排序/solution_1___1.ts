// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e) {
    // 若 数组 不等于 e
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
  }
}

function selectionSort(nums: number[]): number[] {
  // 定义函数/方法 selectionSort
  for (let i = 0; i < nums.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    let minIdx = i; // 把 下标 i 存入 minIdx
    for (let j = i + 1; j < nums.length; j++) {
      // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 数组.长度 就继续
      if (nums[j] < nums[minIdx]) minIdx = j; // 若 数组[下标 j] 小于 数组[minIdx]) minIdx 赋值为 下标 j;
    }
    [nums[i], nums[minIdx]] = [nums[minIdx], nums[i]]; // 把 [数组[minIdx], 数组[下标 i]]; 写入 [nums[i], nums[minIdx]]
  }
  return nums; // 返回 数组
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(selectionSort([1, 2, 3].slice()), [1, 2, 3], 'sel [1,2,3]'); // 断言校验
  assertEq(selectionSort([3, 2, 1].slice()), [1, 2, 3], 'sel [3,2,1]'); // 断言校验
  assertEq(
    selectionSort([5, 2, 4, 1, 3].slice()),
    [1, 2, 3, 4, 5],
    'sel [5,2,4,1,3]',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
