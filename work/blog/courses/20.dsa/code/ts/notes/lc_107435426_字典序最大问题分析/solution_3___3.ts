// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function range_max(ele: number[], i: number): number {
  // 定义函数/方法 range_max
  let mx = ele[i]; // 把 ele[下标 i] 存入 mx
  for (let j = i + 1; j < ele.length; j++) if (ele[j] > mx) mx = ele[j]; // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 ele.长度 就继续
  return mx; // 返回 mx
}
function suffix_max(ele: number[]): number[] {
  // 定义函数/方法 suffix_max
  const n = ele.length; // 把 ele.长度 存入 元素个数
  const res = new Array(n).fill(0); // 把 new Array(元素个数).fill(0) 存入 结果
  res[n - 1] = ele[n - 1]; // 把 ele[元素个数 减 1]; 写入 res[n - 1]
  for (let i = n - 2; i >= 0; i--) res[i] = Math.max(res[i + 1], ele[i]); // 让 下标 i 从 元素个数 减 2 开始计数，下标 i 不低于 0 就继续
  return res; // 返回 结果
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const ele = [4, 1, 3, 5, 2]; // 把 [4, 1, 3, 5, 2] 存入 ele
  assertEq(
    ['range_max(ele, 0) =', range_max(ele, 0)],
    ['range_max(ele, 0) =', 5],
    'rm',
  ); // 断言校验
  assertEq(
    ['suffix_max(ele)    =', suffix_max(ele)],
    ['suffix_max(ele)    =', [5, 5, 5, 5, 2]],
    'sm',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
