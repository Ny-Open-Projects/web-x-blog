// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
// Faithful translation of python reference. Self-check via demo().
function isValid(s: string): boolean {
  // 定义判定函数 isValid
  const stack: string[] = []; // 把 []; 写入 const stack: string[]
  const pairs: { [k: string]: string } = { ')': '(', ']': '[', '}': '{' };
  for (const ch of s) {
    // for (const 字符 of 字符串) {
    if (ch in pairs) {
      // 若 字符 in pairs
      const top = stack.length ? stack.pop()! : '#'; // 把 栈.长度 ? 栈 弹出 )取反 : '#' 存入 top
      if (top !== pairs[ch]) return false; // 若 top 不等于 pairs[字符]，直接返回 false
    } else {
      // 否则
      stack.push(ch); // 把 字符 压入栈/数组尾部
    }
  }
  return stack.length === 0; // 返回 栈.长度 全等于 0
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const tests = ['(', '()', '()[]{}', '(]', '([)]', 'abc']; // 把 ['(', '()', '()[]{}', '(]', '([)]', 'abc'] 存入 tests
  const want = [false, true, true, false, false, false]; // 把 [false, true, true, false, false, false] 存入 want
  for (let i = 0; i < tests.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 tests.长度 就继续
    const got = isValid(tests[i]); // 把 isValid(tests[下标 i]) 存入 got
    if (got !== want[i])
      throw new Error('FAIL test ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
