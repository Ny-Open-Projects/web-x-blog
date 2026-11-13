/**
 ** LeetCode 8. 字符串转换整数 (atoi)
 ** 方案：1 ) 方案1：自动机 (DFA)
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

export function myAtoi(str: string): number {
  // 定义函数/方法 myAtoi
  type State = 'start' | 'signed' | 'in_number' | 'end'; // 定义类型
  const table: { [k in State]: [State, State, State, State] } = {
    start: ['start', 'signed', 'in_number', 'end'],
    signed: ['end', 'end', 'in_number', 'end'],
    in_number: ['end', 'end', 'in_number', 'end'],
    end: ['end', 'end', 'end', 'end'],
  };
  let state: State = 'start'; // 把 '起点'; 写入 let state: State
  let sign = 1; // 把 1 存入 sign
  let ans = 0; // 把 0 存入 答案
  const getCol = (c: string): number => {
    if (c === ' ') return 0; // 若 字符 全等于 ' '，直接返回 0
    if (c === '+' || c === '-') return 1; // 若 字符 全等于 ' 加 ' 或 字符 全等于 ' 减 '，直接返回 1
    if (c >= '0' && c <= '9') return 2; // 若 字符 不低于 '0' 且 字符 不超过 '9'，直接返回 2
    return 3; // 返回 3
  };
  for (const c of str) {
    // for (const 字符 of str) {
    state = table[state][getCol(c)]; // 把 table[state][getCol(字符)] 存入 state
    if (state === 'in_number') {
      // 若 state 全等于 'in_number'
      ans = ans * 10 + parseInt(c, 10); // 把 答案 乘 10 加 转整数(字符) 存入 答案
      if (sign === 1)
        ans = Math.min(ans, 2147483647); // 若 sign 全等于 1) 答案 赋值为 Math.取较小值 答案, 2147483647);
      else ans = Math.min(ans, 2147483648); // 否则
    } else if (state === 'signed') {
      // 否则，若 state 全等于 'signed'
      sign = c === '+' ? 1 : -1; // 把 字符 全等于 ' 加 ' ? 1 : 减 1 存入 sign
    }
  }
  return sign * ans; // 返回 sign 乘 答案
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (myAtoi('   -42') !== -42) throw new Error('FAILED 1'); // 若 myAtoi(「 减 42」) 不等于 减 42) throw new Error(「 减 42」);
  if (myAtoi('4193 with words') !== 4193) throw new Error('FAILED 2');
  if (myAtoi('words and 987') !== 0) throw new Error('FAILED 3');
  if (myAtoi('-91283472332') !== -2147483648)
    throw new Error('FAILED 4: ' + myAtoi('-91283472332'));
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
