// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002

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

function seqSearch(arr: number[], target: number): number {
  // 定义函数/方法 seqSearch
  for (let i = 0; i < arr.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (arr[i] === target) return i; // 若 数组[下标 i] 全等于 目标值，直接返回 下标 i
  }
  return -1; // 返回 减 1
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(seqSearch([1, 2, 3], 1), 0, 'seqSearch hit'); // 断言校验
  assertEq(seqSearch([1, 2, 3], 2), 1, 'seqSearch hit2'); // 断言校验
  assertEq(seqSearch([1, 2, 3], 4), -1, 'seqSearch miss'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
