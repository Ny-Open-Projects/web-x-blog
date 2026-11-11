// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function climb_stairs_count(h: number): number {
  // 定义函数/方法 climb_stairs_count
  if (h < 0) return 0; // 若 h 小于 0，直接返回 0
  if (h === 0) return 1; // 若 h 全等于 0，直接返回 1
  if (h === 1) return 1; // 若 h 全等于 1，直接返回 1
  if (h === 2) return 2; // 若 h 全等于 2，直接返回 2
  const dp = new Array(h + 1).fill(0); // 把 new Array(h 加 1).fill(0) 存入 DP 表
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2; // 把 1; DP 表[1] 赋值为 1; DP 表[2] 赋值为 2; 写入 dp[0]
  for (let i = 3; i <= h; i++) dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]; // 让 下标 i 从 3 开始计数，下标 i 不超过 h 就继续
  return dp[h]; // 返回 DP 表[h]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(climb_stairs_count(4), 7, 's4'); // 断言校验
  assertEq(climb_stairs_count(6), 24, 's6'); // 断言校验
  assertEq(climb_stairs_count(10), 274, 's10'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
