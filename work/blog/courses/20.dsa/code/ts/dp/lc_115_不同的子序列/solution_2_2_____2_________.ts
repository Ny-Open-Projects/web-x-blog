// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function numDistinct(s: string, t: string): number {
  // 定义函数/方法 numDistinct
  const sLen = s.length,
    tLen = t.length; // 把 字符串.长度, tLen 赋值为 另一字符串.长度 存入 sLen
  const memo = new Map<string, number>(); // 把 new Map 小于 string, number 超过 () 存入 记忆化表
  function helper(i: number, j: number): number {
    // 定义函数/方法 helper
    if (j < 0) return 1; // 若 下标 j 小于 0，直接返回 1
    if (i < 0) return 0; // 若 下标 i 小于 0，直接返回 0
    const key = i + ',' + j; // 把 下标 i 加 「,」 加 下标 j 存入 key
    if (memo.has(key)) return memo.get(key)!; // 若 记忆化表.has(key)，直接返回 记忆化表 查找 key)取反
    let res: number; // let 结果: number;
    if (s[i] === t[j]) res = helper(i - 1, j) + helper(i - 1, j - 1);
    else res = helper(i - 1, j); // 否则
    memo.set(key, res); // 记忆化表.set(key, 结果);
    return res; // 返回 结果
  }
  return helper(sLen - 1, tLen - 1); // 返回 helper(sLen 减 1, tLen 减 1)
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(numDistinct('rabbbit', 'rabbit'), 3, 'nd1'); // 断言校验
  assertEq(numDistinct('babgbag', 'bag'), 5, 'nd2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
