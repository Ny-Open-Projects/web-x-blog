// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function frequencySort(s: string): string {
  // 定义函数/方法 frequencySort
  const map: { [k: string]: number } = {}; // 把 {}; 写入 const map: { [k: string]: number }
  for (const ch of s) map[ch] = (map[ch] || 0) + 1; // 把 (映射表[字符] 或 0) 加 1; 写入 for (const ch of s) map[ch]
  const entries = Object.entries(map).sort(
    (a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1),
  );
  let res = ''; // 把 「」 存入 结果
  for (const [ch, cnt] of entries) res += ch.repeat(cnt); // 把 字符.repeat(计数); 写入 for (const [ch, cnt] of entries) res +
  return res; // 返回 结果
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(frequencySort('tree'), 'eert', 'fs'); // 断言校验
  assertEq(frequencySort(''), '', 'empty'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
