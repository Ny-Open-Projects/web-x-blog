// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function match(regexp: string, text: string): boolean {
  // 定义函数/方法 match
  if (regexp && regexp[0] === '^') return matchhere(regexp.slice(1), text);
  let i = 0; // 把 0 存入 下标 i
  while (true) {
    // 循环，直到不满足「true」
    if (matchhere(regexp, text.slice(i))) return true; // 若 matchhere(regexp, text 截取 下标 i))，直接返回 true
    if (i >= text.length) break; // 若 下标 i 不低于 text.长度) break;
    i++; // 下标 i 加一
  }
  return false; // 返回 false
}
function matchhere(regexp: string, text: string): boolean {
  // 定义函数/方法 matchhere
  if (regexp === '') return true; // 若 regexp 全等于 ''，直接返回 true
  if (regexp.length >= 2 && regexp[1] === '*')
    return matchstar(regexp[0], regexp.slice(2), text);
  if (regexp[0] === '$' && regexp.length === 1) return text === ''; // 若 regexp[0] 全等于 '$' 且 regexp.长度 全等于 1，直接返回 text 全等于 ''
  if (text && (regexp[0] === '.' || regexp[0] === text[0]))
    return matchhere(regexp.slice(1), text.slice(1));
  return false; // 返回 false
}
function matchstar(c: string, regexp: string, text: string): boolean {
  // 定义函数/方法 matchstar
  let i = 0; // 把 0 存入 下标 i
  while (true) {
    // 循环，直到不满足「true」
    if (matchhere(regexp, text.slice(i))) return true; // 若 matchhere(regexp, text 截取 下标 i))，直接返回 true
    if (i >= text.length) break; // 若 下标 i 不低于 text.长度) break;
    if (text[i] !== c && c !== '.') break; // 若 text[下标 i] 不等于 字符 且 字符 不等于 '.') break;
    i++; // 下标 i 加一
  }
  return false; // 返回 false
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(match('abc', 'xxabcxx'), true, 'm1'); // 断言校验
  assertEq(match('a.c', 'axc'), true, 'm2'); // 断言校验
  assertEq(match('a*', 'aaaa'), true, 'm3'); // 断言校验
  assertEq(match('^a', 'ba'), false, 'm4'); // 断言校验
  assertEq(match('c$', 'abc'), true, 'm5'); // 断言校验
  assertEq(match('a.*c', 'aXYZc'), true, 'm6'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
