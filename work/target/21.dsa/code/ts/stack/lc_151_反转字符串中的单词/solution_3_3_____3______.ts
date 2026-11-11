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
  let left = 0,
    right = s.length - 1; // 把 0, 右边界 赋值为 字符串.长度 减 1 存入 左边界
  const words: string[] = []; // 把 []; 写入 const words: string[]
  let word: string[] = []; // 把 []; 写入 let word: string[]
  while (left <= right) {
    // 循环，直到不满足「左边界 不超过 右边界」
    if (s[left] === ' ' && word.length) {
      // 若 字符串[左边界] 全等于 ' ' 且 单词.长度
      words.splice(0, 0, word.join('')); // 拼接为字符串
      word = []; // 把 [] 存入 单词
    } else if (s[left] !== ' ') {
      // 否则，若 字符串[左边界] 不等于 ' '
      word.push(s[left]); // 把 字符串[左边界] 压入栈/数组尾部
    }
    left++; // 左边界 加一
  }
  if (word.length) words.splice(0, 0, word.join('')); // 若 单词.长度) 单词列表.splice(0, 0, 单词.join(「」));
  return words.join(' '); // 返回 单词列表.join(「 」)
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(reverseWords('the sky is blue'), 'blue is sky the', 'reverseWords'); // 断言校验
  assertEq(reverseWords('abc'), 'abc', 'reverseWords single'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
