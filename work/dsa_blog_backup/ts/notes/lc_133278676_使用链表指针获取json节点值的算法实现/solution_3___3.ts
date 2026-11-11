// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function get_value_eval(data: any, path: (string | number)[]): any {
  // 定义函数/方法 get_value_eval
  let cur: any = data; // 把 data; 写入 let cur: any
  for (const k of path) cur = cur[k]; // 把 当前值[下标 k]; 写入 for (const k of path) cur
  return cur; // 返回 当前值
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const data = { a: { b: { c: 1 } }, d: { e: 2 } }; // 把 { 数组: { b: { 字符: 1 } }, d: { e: 2 } } 存入 data
  assertEq(get_value_eval(data, ['a', 'b', 'c']), 1, 'p1'); // 断言校验
  assertEq(get_value_eval(data, ['d', 'e']), 2, 'p2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
