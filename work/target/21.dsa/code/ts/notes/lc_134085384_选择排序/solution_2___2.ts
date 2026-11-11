// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function selection_sort(nums: number[]): void {
  // 定义函数/方法 selection_sort
  const length = nums.length; // 把 数组.长度 存入 长度
  for (let i = 0; i < length - 1; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 长度 减 1 就继续
    let min_index = i; // 把 下标 i 存入 min_index
    for (let j = i + 1; j < length; j++) {
      // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 长度 就继续
      if (nums[j] < nums[min_index]) min_index = j; // 若 数组[下标 j] 小于 数组[min_index]) min_index 赋值为 下标 j;
    }
    if (i !== min_index) {
      const t = nums[i];
      nums[i] = nums[min_index];
      nums[min_index] = t;
    }
  }
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const a = [5, 4, 3, 2, 1].slice();
  selection_sort(a); // 把 [5, 4, 3, 2, 1] 截取 ); selection_sort(数组) 存入 数组
  assertEq(a, [1, 2, 3, 4, 5], 'sel'); // 断言校验
  const b = [3, 1, 4, 2].slice();
  selection_sort(b); // 把 [3, 1, 4, 2] 截取 ); selection_sort(b) 存入 b
  assertEq(b, [1, 2, 3, 4], 'sel2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
