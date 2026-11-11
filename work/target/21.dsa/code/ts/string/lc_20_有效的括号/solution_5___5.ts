// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
// Faithful translation of python reference. Self-check via demo().
function isValid2(s: string): boolean {
  // 定义判定函数 isValid2
  let t = s; // 把 字符串 存入 另一字符串
  while (t.includes('()') || t.includes('{}') || t.includes('[]')) {
    t = t.replace('()', '').replace('{}', '').replace('[]', '');
  }
  return t === ''; // 返回 另一字符串 全等于 ''
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const tests = ['(', '()', '()[]{}', '(]', '([)]', 'abc']; // 把 ['(', '()', '()[]{}', '(]', '([)]', 'abc'] 存入 tests
  const want = [false, true, true, false, false, false]; // 把 [false, true, true, false, false, false] 存入 want
  for (let i = 0; i < tests.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 tests.长度 就继续
    const got = isValid2(tests[i]); // 把 isValid2(tests[下标 i]) 存入 got
    if (got !== want[i])
      throw new Error('FAIL test ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
