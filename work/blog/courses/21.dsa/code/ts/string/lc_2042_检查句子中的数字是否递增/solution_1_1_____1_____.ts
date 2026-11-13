/**
 ** LeetCode 2042. 检查句子中的数字是否递增
 ** 方案：1 ) 方案1：直接遍历
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145374488
 ** 忠实翻译自 python/string/lc_2042_.../solution_1_1_____1_____.py
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function isDigitChar(ch: string): boolean {
    // 定义判定函数 isDigitChar
    const c = ch.charCodeAt(0); // 把 字符.charCodeAt(0) 存入 字符
    return c >= 48 && c <= 57; // '0'..'9'，对应 python word[0].isdigit()
  }

  function areNumbersAscending(s: string): boolean {
    // 定义函数/方法 areNumbersAscending
    // python: s.split() 按任意空白分割并忽略首尾空白
    const trimmed = s.trim(); // 把 字符串.trim() 存入 trimmed
    const words: string[] = trimmed.length === 0 ? [] : trimmed.split(/\s+/);
    let prev = 0; // 把 0 存入 前一个
    for (const word of words) {
      // for (const 单词 of 单词列表) {
      if (isDigitChar(word[0])) {
        // 若 isDigitChar(单词[0]
        const num = parseInt(word, 10); // 把 转整数(单词, 10) 存入 num
        if (num <= prev) {
          // 若 num 不超过 前一个
          return false; // 返回 false
        }
        prev = num; // 把 num 存入 前一个
      }
    }
    return true; // 返回 true
  }

  const cases: { in: string; want: boolean }[] = [
    { in: '1 box has 3 blue 4 red 6 green and 12 yellow marbles', want: true }, // normal: 严格递增
    { in: 'hello world 5 x 5', want: false }, // normal: 5 后接 5 不递增
    { in: 'abc', want: true }, // boundary: 无数字
    { in: 'sunset is at 7 51 pm overnight lows of 14 degrees', want: false }, // boundary: 51 后接 14
    { in: '0 1', want: false }, // boundary: 首数字 0 不大于 prev=0
    { in: 'a 1', want: true }, // boundary: 单个数字
    { in: '', want: true }, // boundary: 空串
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = areNumbersAscending(c.in); // 把 areNumbersAscending(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        `FAIL areNumbersAscending(${JSON.stringify(c.in)})=${got} want ${c.want}`,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
