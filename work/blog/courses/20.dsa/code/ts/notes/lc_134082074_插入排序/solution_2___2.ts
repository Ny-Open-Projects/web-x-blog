// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function insertion_sort(nums: number[]): number[] {
  // 定义函数/方法 insertion_sort
  const a = nums.slice();
  const length = a.length; // 把 数组 截取 ); const 长度 赋值为 数组.长度 存入 数组
  for (let i = 1; i < length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 长度 就继续
    const tmp = a[i];
    let j = i; // 把 数组[下标 i]; let 下标 j 赋值为 下标 i 存入 临时变量
    while (j > 0) {
      if (a[j - 1] > tmp) a[j] = a[j - 1];
      else break;
      j--;
    }
    if (i !== j) a[j] = tmp; // 若 下标 i 不等于 下标 j) 数组[下标 j] 赋值为 临时变量;
  }
  return a; // 返回 数组
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], 'rev'); // 断言校验
  assertEq(insertion_sort([1, 2, 3]), [1, 2, 3], 'sorted'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
