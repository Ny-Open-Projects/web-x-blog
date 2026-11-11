// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831489

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function minFlipsMonoIncr(s: string): number {
  // 定义函数/方法 minFlipsMonoIncr
  let one = 0,
    dp = 0; // 把 0, DP 表 赋值为 0 存入 one
  for (const c of s) {
    // for (const 字符 of 字符串) {
    if (c === '0')
      dp = Math.min(one, dp + 1); // 若 字符 全等于 '0') DP 表 赋值为 Math.取较小值 one, DP 表 加 1);
    else one++; // 否则
  }
  return dp; // 返回 DP 表
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(minFlipsMonoIncr('00110'), 1, 'mf'); // 断言校验
  assertEq(minFlipsMonoIncr(''), 0, 'empty'); // 断言校验
  assertEq(minFlipsMonoIncr('1'), 0, 'one'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
