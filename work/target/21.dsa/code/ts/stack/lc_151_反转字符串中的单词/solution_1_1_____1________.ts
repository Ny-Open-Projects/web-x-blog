// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function reverseWords(s: string): string {
  // 定义函数/方法 reverseWords
  return s.trim().split(/\s+/).reverse().join(' '); // 返回 字符串.trim().split( 除以 \字符串 加 除以 ).reverse().join(「 」)
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(reverseWords('the sky is blue'), 'blue is sky the', 'reverseWords'); // 断言校验
  assertEq(reverseWords('abc'), 'abc', 'reverseWords single'); // 断言校验
  assertEq(
    reverseWords('  hello   world  '),
    'world hello',
    'reverseWords spaces',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
