// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function max_sub_array_ic(arr: number[]): number {
  // 定义函数/方法 max_sub_array_ic
  const n = arr.length; // 把 数组.长度 存入 元素个数
  if (n === 0) return 0; // 若 元素个数 全等于 0，直接返回 0
  let gs = arr[0]; // 把 数组[0] 存入 gs
  for (let i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    let s = 0; // 把 0 存入 字符串
    for (let j = i; j < n; j++) {
      // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
      s += arr[j]; // 字符串累加 数组[下标 j]
      if (gs < s) gs = s; // 若 gs 小于 字符串) gs 赋值为 字符串;
    }
  }
  return gs; // 返回 gs
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(max_sub_array_ic([-2, 1, -3, 4, -1, 2, 1]), 6, 'ms1'); // 断言校验
  assertEq(max_sub_array_ic([-1, -2, -3]), -1, 'ms2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
