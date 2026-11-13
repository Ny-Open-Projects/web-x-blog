/**
 ** LeetCode 65. 有效数字
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133920771
 ** 方案：方案4（确定有限状态自动机 DFA，字符原样作为转移键）
 */

function isNumber(s: string): boolean {
  // 定义判定函数 isNumber
  const graph: Record<number, Record<string, number>> = {
    // 把 { 写入 const graph: Record<number, Record<string, number>>
    0: { blank: 0, sign: 1, '.': 2, digit: 6 },
    1: { digit: 6, '.': 2 },
    2: { digit: 3 },
    3: { digit: 3, e: 4 },
    4: { digit: 5, sign: 7 },
    5: { digit: 5 },
    6: { digit: 6, '.': 3, e: 4 },
    7: { digit: 5 },
  };
  let state = 0; // 把 0 存入 state
  for (const ch of s.trim()) {
    // for (const 字符 of 字符串.trim()) {
    let c: string; // let 字符: string;
    if (ch >= '0' && ch <= '9')
      c = 'digit'; // 若 字符 不低于 「0」 且 字符 不超过 「0」) 字符 赋值为 「0」;
    else if (ch === ' ')
      c = 'blank'; // 否则，若 字符 全等于 「 」) 字符 赋值为 「 」;
    else if (ch === '+' || ch === '-')
      c = 'sign'; // 否则，若 字符 全等于 「 加 」 或 字符 全等于 「 加 」) 字符 赋值为 「 加 」;
    else c = ch; // 原样字符（'e' 直接作键；与 Python 参考一致）
    if (!(c in graph[state])) return false; // 若 取反 (字符 in graph[state])，直接返回 false
    state = graph[state][c]; // 把 graph[state][字符] 存入 state
  }
  return state === 3 || state === 5 || state === 6; // 返回 state 全等于 3 或 state 全等于 5 或 state 全等于 6
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (isNumber('0') !== true) throw new Error("isNumber('0') should be true"); // 若 isNumber(「0」) 不等于 true) throw new Error(「0」);
  if (isNumber('abc') !== false)
    // 若 isNumber(「abc」) 不等于 false
    throw new Error("isNumber('abc') should be false"); // throw new Error(「isNumber('abc') should be false」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
