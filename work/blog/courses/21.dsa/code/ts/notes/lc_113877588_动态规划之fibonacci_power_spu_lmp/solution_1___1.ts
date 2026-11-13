// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function fibonacci(n: number, memo: { [k: number]: number } = {}): number {
  // 定义函数/方法 fibonacci
  if (n <= 1) return n; // 若 元素个数 不超过 1，直接返回 元素个数
  if (n in memo) return memo[n]; // 若 元素个数 in 记忆化表，直接返回 记忆化表[元素个数]
  memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
  return memo[n]; // 返回 记忆化表[元素个数]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(fibonacci(10), 55, 'fib10'); // 断言校验
  assertEq(fibonacci(0), 0, 'fib0'); // 断言校验
  assertEq(fibonacci(1), 1, 'fib1'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
