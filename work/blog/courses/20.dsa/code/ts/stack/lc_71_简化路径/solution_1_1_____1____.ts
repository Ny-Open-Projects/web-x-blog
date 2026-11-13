// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145112805

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function simplifyPath(path: string): string {
  // 定义函数/方法 simplifyPath
  const stk: string[] = []; // 把 []; 写入 const stk: string[]
  for (const s of path.split('/')) {
    // for (const 字符串 of 当前路径.split(' 除以 ')) {
    if (!s || s === '.') continue; // 若 取反 字符串 或 字符串 全等于 '.') continue;
    if (s !== '..')
      stk.push(s); // 若 字符串 不等于 '..') 栈 追加 字符串);
    else if (stk.length) stk.pop(); // 否则，若 栈.长度) 栈 弹出 );
  }
  return '/' + stk.join('/'); // 返回 ' 除以 ' 加 栈.join(' 除以 ')
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(simplifyPath('/home/'), '/home', 'simplifyPath'); // 断言校验
  assertEq(simplifyPath('/a/./b/../../c/'), '/c', 'simplifyPath2'); // 断言校验
  assertEq(simplifyPath('/../'), '/', 'simplifyPath3'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
