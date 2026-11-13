// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
// Faithful translation of python reference. Self-check via demo().
function isValid3(s: string): boolean {
  // 定义判定函数 isValid3
  if (s.length % 2 === 1) return false; // 若 字符串.长度 对…取模 2 全等于 1，直接返回 false
  const pairs: { [k: string]: string } = { ')': '(', '}': '{', ']': '[' };
  const stack: string[] = []; // 把 []; 写入 const stack: string[]
  for (const c of s) {
    // for (const 字符 of 字符串) {
    if (c in pairs) {
      // 若 字符 in pairs
      if (!stack.length || stack[stack.length - 1] !== pairs[c]) return false; // 若 取反 栈.长度 或 栈[栈.长度 减 1] 不等于 pairs[字符]，直接返回 false
      stack.pop(); // 弹出栈顶元素
    } else {
      // 否则
      stack.push(c); // 把 字符 压入栈/数组尾部
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
    const got = isValid3(tests[i]); // 把 isValid3(tests[下标 i]) 存入 got
    if (got !== want[i])
      throw new Error('FAIL test ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
